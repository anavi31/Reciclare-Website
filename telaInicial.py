import streamlit as st

st.set_page_config(
    page_title="Reciclare",
    page_icon="planta.png",
    layout="wide"
)

with open("telaInicial.css") as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

st.markdown("""
<header class="header">
    <div class="logo-container">
        <img src="https://pbs.twimg.com/media/GdKDgEnXYAAKJ7o?format=webp&name=tiny" class="logo">
        <span class="site-name">Reciclare</span>
    </div>
    <div class="header-button-container">
        <a href="st.button("https://Reciclare_Website.render.com/login")
">Login</a>
        <a href="href="https://Reciclare_Website.com/cadastro")
">Cadastro</a>
    </div>
</header>
""", unsafe_allow_html=True)

col1, col2 = st.columns([7,3])

with col1:
    st.markdown("""
    <div class="container">
        <p class="slogan">Reciclare: Pequenas ações, grandes mudanças. Juntos, por um futuro sustentável.</p>
        <h1 class="title">Reciclare: Transformando o hoje para preservar o amanhã.</h1>
        <p class="description">
            Bem-vindo ao Reciclare! Nosso objetivo é promover o descarte responsável de resíduos e incentivar hábitos sustentáveis.
            Acreditamos que pequenas ações, como separar corretamente o lixo, podem fazer grande diferença.
            No Reciclare, você encontra informações e dicas para contribuir com a preservação do meio ambiente.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <center>
        <img src="https://pbs.twimg.com/media/GdgsWw2XAAAQosA?format=png&name=360x360" class="image">
    </center>
    """, unsafe_allow_html=True)