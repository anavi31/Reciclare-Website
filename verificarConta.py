import streamlit as st
import pandas as pd
import os

def add_css(verificarConta):
    with open(verificarConta) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
    page_title="Verificar Conta",
    page_icon="📧",
    layout="wide"
)

add_css("verificarConta.css")

DB_PATH = "codigos_senha.csv"

def carregar_codigo(email):
    if not os.path.exists(DB_PATH):
        return None
    df = pd.read_csv(DB_PATH)
    usuario = df[df["Email"] == email]
    if not usuario.empty:
        return usuario["Código"].values[0]
    return None

col1, col2 = st.columns([2, 3])

with col1:
    st.markdown("<h1 class='title'>Inserir Código</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p class='instruction'>Nós enviaremos um código de 4 dígitos para o seu endereço de e-mail para que você possa redefinir a sua senha.</p>",
        unsafe_allow_html=True,
    )
    email = st.text_input("Digite seu e-mail para verificar o código", placeholder="Digite seu e-mail")
    codigo_digitado = st.text_input("Insira o código de confirmação (apenas números)", max_chars=4, type="password", placeholder="0000")

    if st.button("Confirmar"):
        codigo_enviado = carregar_codigo(email)
        if not codigo_enviado:
            st.error("E-mail não encontrado. Por favor, reinicie o cadastro.")
        elif codigo_digitado == str(codigo_enviado):
            st.success("Código verificado com sucesso!")
            st.markdown(f"""
                    <a href="http://localhost:8508/" target="_self">
                        <button style="
                            background-color: #7a9f84; 
                            color: white; 
                            padding: 10px 24px; 
                            border: none; 
                            border-radius: 5px; 
                            cursor: pointer; 
                            font-size: 16px;
                            font-family: Arial, sans-serif;
                            margin-top: 30px;
                            margin-left: 170px">
                            Redefinir a senha
                        </button>
                    </a>
                """, unsafe_allow_html=True)
        else:
            st.error("Código incorreto. Tente novamente.")

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
    st.markdown(
        """
        <div class="right-section">
            <h1>Reciclare</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )
