import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(
    page_title="Reciclare",
    page_icon="planta.png",
    layout="wide"
)

def add_css(telaLogin):
    with open(telaLogin) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

add_css("telaLogin.css")

col1, col2 = st.columns([2, 3])

with col1:
    st.markdown("<h1>Bem vindo de volta!</h1>", unsafe_allow_html=True)
    st.markdown("<p>Insira as suas credenciais</p>", unsafe_allow_html=True)

    email = st.text_input("Endereço de email", placeholder="Insira seu endereço de email")
    
    password = st.text_input("Senha", placeholder="Digite sua senha", type="password")
    st.markdown('<p><a href="#" style="color: #007bff; text-decoration: none;">Esqueci a senha?</a></p>', unsafe_allow_html=True)

    lembrar = st.checkbox("Lembrar-se") #vai deixar?

    if st.button("Login"):
        st.success("Login realizado com sucesso!")

    st.markdown('<p class="register">Não tem uma conta? <a href="#">Inscrever-se</a></p>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="right-section">Reciclare</div>', unsafe_allow_html=True)
