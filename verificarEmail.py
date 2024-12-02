import streamlit as st
import random
import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "suportereciclare@gmail.com"
EMAIL_PASSWORD = "qwyy rdwi ctjy qckp" 

def add_css(verificarEmail):
    with open(verificarEmail) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
    page_title="Verificar E-mail",
    page_icon="https://pbs.twimg.com/media/GdKDgEnXYAAKJ7o?format=webp&name=tiny",
    layout="wide"
)

add_css("verificarEmail.css")

@st.cache_data
def load_user_emails(file_path):
    try:
        data = pd.read_csv(file_path)
        if "Email" in data.columns:
            return data["Email"].tolist()
        else:
            st.error("O arquivo CSV não contém uma coluna 'Email'.")
            return []
    except Exception as e:
        st.error(f"Erro ao carregar o arquivo CSV: {e}")
        return []

def salvar_codigo(file_path, email, codigo):
    try:
        if not os.path.exists(file_path):
            pd.DataFrame(columns=["Email", "Código"]).to_csv(file_path, index=False)
        
        data = pd.read_csv(file_path)
    
        novo_registro = pd.DataFrame({"Email": [email], "Código": [int(codigo)]})
        data = pd.concat([data, novo_registro], ignore_index=True)
        data.to_csv(file_path, index=False)
    except Exception as e:
        st.error(f"Erro ao salvar o código no arquivo CSV: {e}")
        
def enviar_codigo(email):
    codigo = random.randint(1000, 9999)
    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL_SENDER
        msg["To"] = email
        msg["Subject"] = "Código de Verificação - Reciclare"
        body = f"Seu código de verificação para redefinir sua senha é: {codigo}\n\nSe você não solicitou este código, ignore esta mensagem."
        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, email, msg.as_string())

        return codigo
    except Exception as e:
        st.error(f"Falha ao enviar o e-mail: {e}")
        return None

database_emails = load_user_emails("dados_usuarios.csv")

col1, col2 = st.columns([2, 3])

with col1:
    st.markdown("<h1>Redefina sua senha</h1>", unsafe_allow_html=True)
    st.markdown('<label for="email">Insira seu endereço de E-mail cadastrado</label>', unsafe_allow_html=True)
    email = st.text_input("", placeholder="Insira o seu endereço de e-mail. Ex.: joao9554@gmail.com")
    
    if st.button("Confirmar"):
        if email in database_emails:
            codigo = enviar_codigo(email)
            if codigo:
                salvar_codigo("codigos_senha.csv", email, codigo)
                st.success("Uma mensagem foi enviada ao seu e-mail para a autenticação!")
                st.markdown("""
                <a href="http://localhost:8508/">
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
                        Confirmar Codigo
                    </button>
                </a>
            """, unsafe_allow_html=True)

        else:
            st.error("Nenhuma conta vinculada a este e-mail foi encontrada.")
            
           
    margem_superior = 230 
    posicao_esquerda = -80  

    st.markdown(
        f'''
        <img src="https://pbs.twimg.com/media/GdgsWw2XAAAQosA?format=png&name=360x360" 
        style="position: relative; top: {margem_superior}px; left: {posicao_esquerda}px; width: 50%;">
        ''',
        unsafe_allow_html=True
    )

with col2:
    st.markdown('<div class="right-section">Reciclare</div>', unsafe_allow_html=True)