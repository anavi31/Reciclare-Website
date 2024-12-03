import streamlit as st
import pandas as pd
import re

st.set_page_config(
    page_title="Reciclare",
    page_icon="planta.png",
    layout="wide"
)

def add_css(telaLogin):
    with open(telaLogin) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

add_css("telaLogin.css")

def is_valid_email(email):
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_regex, email) is not None

@st.cache_data
def load_user_data(file_path):
    try:
        data = pd.read_csv(file_path)
        
        if all(col in data.columns for col in ["Nome de Usuario","Email","Senha","Bairro"]):
            data["Senha"] = data["Senha"].astype(str).str.strip()
            return data.set_index("Email")["Senha"].to_dict()
        else:
            st.error("Arquivo CSV não possui as colunas esperadas: 'Nome de Usuario', 'Email', 'Senha' e 'Bairro'.")
            return {}
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")
        return {}

user_database = load_user_data("dados_usuarios.csv")

col1, col2 = st.columns([2, 3])

with col1:
    st.markdown("<h1>Bem vindo de volta!</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Insira as suas credenciais</h3>", unsafe_allow_html=True)
  
    email = st.text_input("Endereço de email", placeholder="Insira seu endereço de email")
    password = st.text_input("Senha", placeholder="Digite sua senha", type="password")
    
    st.markdown('<p><a href="http://localhost:8506/" style="color: #007bff; text-decoration: none; font-size: 0.8em;">Esqueci a senha</a></p>', unsafe_allow_html=True)
    lembrar = st.checkbox("Lembrar-se")
  
    if st.button("Confirmar"):
        if not email or not password:
            st.error("Por favor, preencha todos os campos.")
        elif not is_valid_email(email):
            st.error("Por favor, insira um email válido.")
        elif email not in user_database:
            st.error("Conta não encontrada. Verifique o email ou inscreva-se.")
        elif user_database[email] != password.strip():
            st.error("Senha inválida.")
        else:
            st.session_state["usuario_logado"] = email

            st.success(f"Credenciais validadas, clique no botão abaixo para se conectar!")
            st.markdown(f"""
            <a href="http://localhost:8509/?usuario={email}">
                <button style="
                    background-color: #7a9f84;
                    color: white;
                    padding: 10px 24px;
                    border: 0;
                    cursor: pointer;
                    font-size: 16px;
                    border-radius: 5px;
                    margin-top: 30px;
                    margin-left: 277px">
                    Conectar-se
                </button>
            </a>""", unsafe_allow_html=True)

            
    st.markdown('<p class="register">Não tem uma conta? <a href="http://localhost:8506/">Inscrever-se</a></p>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="right-section">Reciclare</div>', unsafe_allow_html=True)
