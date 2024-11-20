import streamlit as st

st.set_page_config(page_title="Alterar Senha", page_icon="🔒", layout="wide")

def load_css_from_file(alterarSenha):
    with open(alterarSenha) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css_from_file("alterarSenha.css")

st.markdown('<div class="container">', unsafe_allow_html=True)

st.markdown('<div class="left-section">', unsafe_allow_html=True)
st.markdown("<h1>Alterar Senha</h1>", unsafe_allow_html=True)
st.markdown(
    "<p>Insira uma senha diferente para a alteração.</p>",
    unsafe_allow_html=True,
)

nova_senha = st.text_input("Nova Senha", type="password", key="nova_senha", placeholder="Digite a nova senha")
confirma_senha = st.text_input("Confirme sua senha", type="password", key="confirma_senha", placeholder="Confirme a nova senha")

if st.button("Alterar Senha"):
    if nova_senha and confirma_senha:
        if nova_senha == confirma_senha:
            st.success("Senha alterada com sucesso!")
        else:
            st.error("As senhas não coincidem. Por favor, tente novamente.")
    else:
        st.warning("Preencha ambos os campos.")

st.markdown('<img src="mascote.png" class="mascote">', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="right-section">Reciclare</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)