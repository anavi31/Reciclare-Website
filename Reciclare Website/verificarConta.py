import streamlit as st

def add_css(verificarConta):
    with open(verificarConta) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
    page_title="Verificar Conta",
    page_icon="📧",
    layout="wide"
)

add_css("verificarConta.css")

col1, col2 = st.columns([2, 3])

with col1:
    st.markdown("<h1 class='title'>Verificar Conta</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p class='instruction'>Nós enviaremos um código de 4 dígitos para o seu endereço de e-mail.</p>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="code-inputs">
            <input type="text" maxlength="1">
            <input type="text" maxlength="1">
            <input type="text" maxlength="1">
            <input type="text" maxlength="1">
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="button-container">
            <button class="confirm-button">Confirmar</button>
        </div>
        """,
        unsafe_allow_html=True,
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
