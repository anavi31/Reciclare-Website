import streamlit as st

with open("telaUser.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""
<header class="header">
    <div class="logo-container">
        <img src="https://pbs.twimg.com/media/GdKDgEnXYAAKJ7o?format=webp&name=tiny" class="logo">
        <span class="site-name">Reciclare</span>
    </div>
    <div class="header-button-container">
        <a href="">Tela Inicial</a>
        <a href="">Gráficos</a>
        <a href="">Ranking</a>
    </div>
</header>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1,1])

with col1:
    st.markdown(f"""
    <div class="mensagem-card">
        <h1 class="mensagem">Olá reciclinho!</h1>           
        <div class="card">
            <img src="https://pbs.twimg.com/media/GdwTJuyXsAA3_Ju?format=jpg&name=360x360" alt="Imagem do usuário" class="card-image">
            <div class="card-body">
                <p class="card-header">Reciclare</p>
                <p><strong>Nome:</strong> Reciclinho</p>
                <p><strong>Bairro:</strong> Paralela</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown('<div class="checkbox-container">', unsafe_allow_html=True)

    st.markdown("<h3>Informe a quantidade de resíduos que você recicla:</h3>", unsafe_allow_html=True)

    papel_papelao = st.number_input("Papel e Papelão", min_value=0, step=1, value=0, format="%d")
    vidro = st.number_input("Vidro", min_value=0, step=1, value=0, format="%d")
    plastico = st.number_input("Plástico", min_value=0, step=1, value=0, format="%d")
    metais = st.number_input("Metais", min_value=0, step=1, value=0, format="%d")
    organicos = st.number_input("Resíduos Orgânicos", min_value=0, step=1, value=0, format="%d")

    if st.button("Enviar"):
        residuos = {
            "Papel e Papelão": papel_papelao,
            "Vidro": vidro,
            "Plástico": plastico,
            "Metais": metais,
            "Resíduos Orgânicos": organicos,
        }
        
        if any(qty > 0 for qty in residuos.values()):
            resultado = "\n".join([f"{tipo}: {quantidade}" for tipo, quantidade in residuos.items() if quantidade > 0])
            st.success(f"Você informou as seguintes quantidades:\n{resultado}")
        else:
            st.warning("Por favor, insira a quantidade de pelo menos um tipo de resíduo.")

        st.markdown('</div>', unsafe_allow_html=True)