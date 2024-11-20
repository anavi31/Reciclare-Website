import streamlit as st

def add_css(verificarEmail):
    with open(verificarEmail) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
    page_title="Verificar E-mail",
    page_icon="📧",
    layout="wide"
)

add_css("verificarEmail.css")

col1, col2 = st.columns([2, 3])

with col1:
    st.markdown("<h1>Verificar E-mail</h1>", unsafe_allow_html=True)
    st.markdown('<label for="email">Endereço de E-mail</label>',
                unsafe_allow_html=True)
    email = st.text_input(
        "", placeholder="Insira o seu endereço de e-mail. Ex.: joao9554@gmail.com")
    if st.button("Confirmar"):
        st.success("Uma mensagem foi enviada ao seu e-mail para a autenticação!")

    st.markdown(
        '<img src="mascote.png" style="bottom: 50px; top: 500px; left: 10px; width: 50px;">',
        unsafe_allow_html=True
    )

with col2:
    st.markdown('<div class="right-section">Reciclare</div>',
                unsafe_allow_html=True)
