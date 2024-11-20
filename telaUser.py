import streamlit as st

# Carregar estilo CSS
with open("telaUser.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Layout da página
st.markdown('<div class="header">Olá Reciclinho!</div>', unsafe_allow_html=True)

# Cartão de perfil
st.markdown("""
<div class="card">
    <div class="card-header">Reciclare</div>
    <div class="card-body">
        <p><strong>Nome:</strong> Reciclinho</p>
        <p><strong>Bairro:</strong> Paralela</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Seleção de categorias
categories = ["Papel e Papelão", "Vidro", "Plástico", "Metais", "Resíduos Orgânicos"]
selected_categories = st.multiselect("Selecione os tipos de resíduos que você recicla:", categories)

if st.button("Enviar"):
    st.success("Informações salvas com sucesso!")
