import streamlit as st
import re
import random
import smtplib
from email.message import EmailMessage
import pandas as pd
import os

st.set_page_config(page_title="Cadastro", page_icon="📝", layout="wide")

def load_css(telaCadastro):
    with open(telaCadastro) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("telaCadastro.css") 

def email_valido(email):
    return re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.com$", email) is not None

def enviar_codigo(email, nome_usuario):
    remetente = "suportereciclare@gmail.com"
    senha_remetente = "qwyy rdwi ctjy qckp"
    codigo = random.randint(1000, 9999)

    msg = EmailMessage()
    msg['Subject'] = 'Código de Confirmação - Cadastro'
    msg['From'] = remetente
    msg['To'] = email
    msg.set_content(f"""
Olá, {nome_usuario}!

Seu código de confirmação é: {codigo}

Obrigado por se cadastrar!

Atenciosamente, 
Equipe Reciclare
""")

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(remetente, senha_remetente)
            server.send_message(msg)
        return codigo
    except Exception as e:
        st.error(f"Erro ao enviar o código: {e}")
        return None

DB_PATH = "codigos.csv"

def salvar_codigo(email, codigo):
    if os.path.exists(DB_PATH):
        df = pd.read_csv(DB_PATH)
    else:
        df = pd.DataFrame(columns=["email", "codigo"])

    novo_codigo = pd.DataFrame([{"email": email, "codigo": int(codigo)}])
    df = pd.concat([df, novo_codigo], ignore_index=True)
    df.to_csv(DB_PATH, index=False)

def salvar_dados_usuario(nome_usuario, email, bairro, senha):
    DB_USUARIOS_PATH = "dados_usuarios.csv"
    if os.path.exists(DB_USUARIOS_PATH):
        df = pd.read_csv(DB_USUARIOS_PATH)
    else:
        df = pd.DataFrame(columns=["Nome de Usuário", "Email", "Bairro", "Senha"])

    novo_usuario = pd.DataFrame([{
        "Nome de Usuário": nome_usuario,
        "Email": email,
        "Bairro": bairro,
        "Senha": senha
    }])
    
    df = pd.concat([df, novo_usuario], ignore_index=True)
    df.to_csv(DB_USUARIOS_PATH, index=False)


col1, col2 = st.columns([2, 3])

with col1:
    st.title("Cadastro")
    nome_usuario = st.text_input("Nome de Usuário", placeholder="Crie seu nome de usuário")
    email = st.text_input("Endereço de Email", placeholder="Digite seu e-mail")
    bairro = st.selectbox("Bairro", ["--Selecionar--", "Bonfim", "Cabula", "Paralela", "Sussuarana"])
    senha = st.text_input("Senha", type="password", placeholder="Crie uma senha")
    confirma_senha = st.text_input("Confirme sua Senha", type="password", placeholder="Digite a senha")
    aceita_termos = st.checkbox("Eu concordo com os Termos e Política de Privacidade")

    if st.button("Cadastrar-se"):
        if not nome_usuario or not email or not senha or not confirma_senha or bairro == "--Selecionar--":
           st.error("Por favor, preencha todos os campos.")
        elif not email_valido(email):
           st.error("Por favor, insira um e-mail válido.")
        elif senha != confirma_senha:
           st.error("As senhas não coincidem!")
        elif not aceita_termos:
           st.warning("Você deve aceitar os termos para continuar.")
        else:
            codigo = enviar_codigo(email, nome_usuario)
            if codigo:
             st.session_state["codigo_confirmacao"] = codigo
             salvar_codigo(email, codigo)
             salvar_dados_usuario(nome_usuario, email, bairro, senha) 
             st.session_state["dados_usuario"] = {
                "Nome de Usuário": nome_usuario,
                "Email": email,
                "Bairro": bairro,
                "Senha": senha,
              }
            st.success("Código enviado! Agora, clique no botão abaixo para ir à tela de verificação.")
            
            st.markdown("""
                <a href="http://localhost:8501/">
                    <button style="
                        background-color: #7a9f84;
                        color: white;
                        padding: 10px 24px;
                        border: 0;
                        cursor: pointer;
                        font-size: 16px;
                        border-radius: 5px;
                        margin-top: 30px;
                        margin-left: 170px">
                        Ir para a Tela de Inserção do Código
                    </button>
                </a>
            """, unsafe_allow_html=True)

with col2:
    st.markdown('<div class="right-section">Reciclare</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
