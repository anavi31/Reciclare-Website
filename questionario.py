import streamlit as st

# Carregar estilo CSS
with open("questionario.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Layout da página
st.markdown('<div class="header">Pergunta 1</div>', unsafe_allow_html=True)

st.markdown('<div class="question">Você separa os materiais recicláveis (plástico, vidro, metal) dos resíduos orgânicos em casa?</div>', unsafe_allow_html=True)

# Opções de resposta
options = ["Sim", "Um pouco", "Não sei dizer", "Não muito", "Não"]
selected = st.radio("", options, index=4, horizontal=True)

# Botão Continuar
if st.button("CONTINUE"):
    st.success("Resposta registrada!")
