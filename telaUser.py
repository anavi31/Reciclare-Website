import streamlit as st
import pandas as pd
import csv
import unicodedata

def normalize_text(text):
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')

with open("telaUser.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

if "usuario_logado" not in st.session_state:
    st.session_state["usuario_logado"] = None

query_params = st.query_params

if "usuario" in query_params:
    st.session_state["usuario_logado"] = query_params["usuario"]

if st.session_state["usuario_logado"] is None:
    st.warning("Você precisa estar logado para registrar resíduos.")
    st.stop()

email_logado = st.session_state["usuario_logado"]
usuarios = pd.read_csv("dados_usuarios.csv", encoding="utf-8")

try:
    usuario_info = usuarios.loc[usuarios["Email"] == email_logado].iloc[0]
    nome_usuario = normalize_text(usuario_info["Nome de Usuario"])
    bairro_usuario = usuario_info["Bairro"]
    ranking_usuario = normalize_text(usuario_info["Ranking"])
except IndexError:
    st.error("Não foi possível encontrar o nome do usuário. Verifique os dados cadastrados.")
    st.stop()

usuario = st.session_state["usuario_logado"]

st.markdown("""
<header class="header">
    <div class="logo-container">
        <img src="https://pbs.twimg.com/media/GdKDgEnXYAAKJ7o?format=webp&name=tiny" class="logo">
        <span class="site-name">Reciclare</span>
    </div>
    <div class="header-button-container">
        <a href="http://localhost:8510/">Infos</a>
        <a href="http://localhost:8512/">Gráficos</a>
        <a href="http://localhost:8511/">Ranking</a>
    </div>
</header>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1,1])

with col1:
    st.markdown(f"""
        <h1 class="mensagem">Olá reciclinho!</h1>           
        <div class="card">
            <img src="https://pbs.twimg.com/media/GdwTJuyXsAA3_Ju?format=jpg&name=360x360" alt="Imagem do usuário" class="card-image">
            <div class="card-body">
                <p class="card-header">Reciclare</p>
                <p><strong>Nome:</strong>{nome_usuario}</p>
                <p><strong>Bairro:</strong>{bairro_usuario}</p>
                <p><strong>Ranking:</strong>{ranking_usuario}</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("<h3>Selecione as unidades de resíduos descartados:</h3>", unsafe_allow_html=True)
    
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
            try:
                df_residuos = pd.read_csv("residuos.csv")
            except FileNotFoundError:
                df_residuos = pd.DataFrame(columns=["Email", "Tipo de Resíduo", "Quantidade", "Data"])

            data_atual = pd.to_datetime("now").strftime("%Y-%m-%d")

            novos_registros = []
            for tipo, quantidade in residuos.items():
                if quantidade > 0:
                    novos_registros.append({
                        "Email": email_logado,
                        "Tipo de Resíduo": tipo,
                        "Quantidade": quantidade,
                        "Data": data_atual,
                    })

            df_residuos = pd.concat([df_residuos, pd.DataFrame(novos_registros)], ignore_index=True)
            df_residuos.to_csv("residuos.csv", index=False)
            st.success("Resíduos registrados com sucesso!")
        else:
            st.warning("Por favor, insira a quantidade de pelo menos um tipo de resíduo.")
