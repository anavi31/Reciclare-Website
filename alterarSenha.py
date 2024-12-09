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
                    
                    st.markdown(f"""
                    <a href="http://localhost:8502/" target="_self">
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
                            Faça login novamente
                        </button>
                    </a>
                """, unsafe_allow_html=True)
                    
                else:
                    st.error(mensagem)
            else:
                st.error("As senhas não coincidem. Por favor, tente novamente.")
        else:
            st.warning("Preencha todos os campos.")
            
    margem_superior = 230 
    posicao_esquerda = -80  

    st.markdown(
        f'''
        <img src="https://pbs.twimg.com/media/GdgsWw2XAAAQosA?format=png&name=360x360" 
        style="position: relative; top: 90px; left: {posicao_esquerda}px; width: 330px;">
        ''',
        unsafe_allow_html=True
    )
                      

with col2:
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="right-section">Reciclare</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)