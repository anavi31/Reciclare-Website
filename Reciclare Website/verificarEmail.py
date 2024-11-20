import streamlit as st

# Função para carregar o CSS
def add_css(verificarEmail):
    with open(verificarEmail) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Configurações da página
st.set_page_config(
    page_title="Verificar E-mail",
    page_icon="📧",
    layout="wide"
)

# Adicionar o CSS personalizado
add_css("verificarEmail.css")

# Layout da página
col1, col2 = st.columns([2, 3])

# Painel esquerdo
with col1:
    st.markdown("<h1>Verificar E-mail</h1>", unsafe_allow_html=True)
    st.markdown('<label for="email">Endereço de E-mail</label>', unsafe_allow_html=True)
    email = st.text_input("", placeholder="Insira o E-mail: joao9554@gmail.com")
    if st.button("Confirmar"):
        st.success("E-mail enviado para verificação!")

    # Ícone no canto inferior esquerdo
    st.markdown(
        '<img src="https://path-to-your-icon.png" alt="Ícone" style="position: absolute; bottom: 10px; left: 10px; width: 50px;">',
        unsafe_allow_html=True
    )

# Painel direito
with col2:
    st.markdown('<div class="right-section">Reciclare</div>', unsafe_allow_html=True)