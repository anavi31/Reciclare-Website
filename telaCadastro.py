import streamlit as st

st.set_page_config(page_title="Cadastro", page_icon="📝", layout="wide")

def load_css(telaCadastro):
    with open(telaCadastro) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("telaCadastro.css")

st.markdown('<div class="container">', unsafe_allow_html=True)

st.markdown('<div class="left-section">', unsafe_allow_html=True)
st.markdown("<h1>Cadastro</h1>", unsafe_allow_html=True)

nome_usuario = st.text_input("Nome de Usuário", placeholder="Crie seu nome de usuário")
email = st.text_input("Endereço de Email", placeholder="Digite seu e-mail")
bairro = st.selectbox("Bairro", ["--Selecionar--", "Bairro 1", "Bairro 2", "Bairro 3"])
senha = st.text_input("Senha", type="password", placeholder="Crie uma senha")
confirma_senha = st.text_input("Confirme sua Senha", type="password", placeholder="Digite a senha")

aceita_termos = st.checkbox("Eu concordo com os Termos e Política de Privacidade")

if st.button("Cadastrar-se"):
    if aceita_termos:
        if senha == confirma_senha:
            st.success("Cadastro realizado com sucesso!")
        else:
            st.error("As senhas não coincidem!")
    else:
        st.warning("Você deve aceitar os termos para continuar.")

st.markdown('<p class="footer">Não tem uma conta? <a href="#">Inscrever-se</a></p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="right-section">Reciclare</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)