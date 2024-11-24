import streamlit as st
import re

st.set_page_config(
    page_title="Reciclare",
    page_icon="https://pbs.twimg.com/media/GdKDgEnXYAAKJ7o?format=webp&name=tiny",
    layout="wide"
)

def add_css(telaLogin):
    with open(telaLogin) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

add_css("telaLogin.css")

database = {
    "usuario1@email.com": "senha123",
    "admin@reciclare.com": "admin2024",
    "contato@site.com": "contato@123",
    "miguel0205brgg@gmail.com": "miguelSenha"
}

def is_valid_email(email):
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_regex, email) is not None

col1, col2 = st.columns([2, 3])

with col1:
    st.markdown("<h1>Bem vindo de volta!</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Insira as suas credenciais</h3>", unsafe_allow_html=True)
  
    email = st.text_input("Endereço de email", placeholder="Insira seu endereço de email")
  
    password = st.text_input("Senha", placeholder="Digite sua senha", type="password")
    
    st.markdown('<p><a href="#" style="color: #007bff; text-decoration: none; font-size: 0.8em;">Esqueci a senha</a></p>', unsafe_allow_html=True)

    lembrar = st.checkbox("Lembrar-se")
  
    if st.button("Login"):
        if not email or not password:
            st.error("Por favor, preencha todos os campos.")
        elif not is_valid_email(email):
            st.error("Por favor, insira um email válido.")
        elif email not in database:
            st.error("Conta não encontrada. Verifique o email ou inscreva-se.")    
        elif database[email] != password:
            st.error("Senha inválida.")
        else:
            st.success("Login realizado com sucesso!")
            
    st.markdown('<p class="register">Não tem uma conta? <a href="#">Inscrever-se</a></p>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="right-section">Reciclare</div>', unsafe_allow_html=True)