import streamlit as st
import pandas as pd

st.set_page_config(page_title="Alterar Senha", page_icon="🔒", layout="wide")

def load_css_from_file(alterarSenha):
    with open(alterarSenha) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css_from_file("alterarSenha.css")

col1, col2 = st.columns([2, 3])

with col1:
    st.markdown('<div class="container">', unsafe_allow_html=True)
    st.markdown('<div class="left-section">', unsafe_allow_html=True)
    st.markdown("<h1>Alterar Senha</h1>", unsafe_allow_html=True)
    st.markdown("<p>Insira uma senha diferente para a alteração.</p>", unsafe_allow_html=True)

    usuario = st.text_input("Nome de Usuário", key="usuario", placeholder="Digite seu nome de usuário")
    nova_senha = st.text_input("Nova Senha", type="password", key="nova_senha", placeholder="Digite a nova senha")
    confirma_senha = st.text_input("Confirme sua senha", type="password", key="confirma_senha", placeholder="Confirme a nova senha")

    def atualizar_senha_csv(usuario, nova_senha, caminho_csv):
        try:
            df = pd.read_csv(caminho_csv)
        
            if usuario in df['Nome de Usuário'].values:
             df.loc[df['Nome de Usuário'] == usuario, 'Senha'] = nova_senha
             df.to_csv(caminho_csv, index=False)
             return True, "Senha alterada com sucesso!"
            else:
             return False, "Usuário não encontrado no sistema."
        except Exception as e:
         return False, f"Erro ao atualizar a senha: {e}"

    if st.button("Alterar Senha"):
        if usuario and nova_senha and confirma_senha:
            if nova_senha == confirma_senha:
                sucesso, mensagem = atualizar_senha_csv(usuario, nova_senha, 'dados_usuarios.csv')
                if sucesso:
                    st.success(mensagem)
                else:
                    st.error(mensagem)
            else:
                st.error("As senhas não coincidem. Por favor, tente novamente.")
        else:
            st.warning("Preencha todos os campos.")

with col2:
    st.markdown('<img src="https://pbs.twimg.com/media/GdgsWw2XAAAQosA?format=png&name=360x360" class="mascote">', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="right-section">Reciclare</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
