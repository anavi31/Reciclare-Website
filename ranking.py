import pandas as pd
import streamlit as st

st.set_page_config(page_title="Ranking de Reciclagem", layout="wide")

with open("ranking.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""
<header class="header">
    <div class="logo-container">
        <img src="https://pbs.twimg.com/media/GdKDgEnXYAAKJ7o?format=webp&name=tiny" class="logo">
        <span class="site-name">Reciclare</span>
    </div>
    <div class="header-button-container">
        <a href=""></a>
        <a href="">Gráficos</a>
        <a href="http://localhost:8510/">Informações</a>
    </div>
</header>
""", unsafe_allow_html=True)

residuos = pd.read_csv("residuos.csv")
usuarios = pd.read_csv("dados_usuarios.csv")

bairro_usuario = "Sussuarana"
usuarios = usuarios[usuarios["Bairro"] == bairro_usuario]

residuos_somados = residuos.groupby("Email")["Quantidade"].sum().reset_index()
dados_usuarios_totais = pd.merge(usuarios, residuos_somados, on="Email")
ranking = residuos_somados.sort_values("Quantidade", ascending=False)

st.markdown('<div class="footer"></div>', unsafe_allow_html=True)


col1, col2 = st.columns([1,1])

with col1:

    top_3 = dados_usuarios_totais.nlargest(3, "Quantidade")[["Nome de Usuario", "Quantidade"]]
    top_3.columns = ["Usuario", "Reciclados"]
    top_3 = top_3.to_dict(orient="records")

    st.markdown(
        f"""
        <div class="podium">
            <div class="second">
                <div class="medal">🥈</div>
                <h2>{top_3[1]["Usuario"]}</h2>
                <p>{top_3[1]["Reciclados"]} Reciclados</p>
            </div>
            <div class="first">
                <div class="medal">🥇</div>
                <h2>{top_3[0]["Usuario"]}</h2>
                <p>{top_3[0]["Reciclados"]} Reciclados</p>
            </div>
            <div class="third">
                <div class="medal">🥉</div>
                <h2>{top_3[2]["Usuario"]}</h2>
                <p>{top_3[2]["Reciclados"]} Reciclados</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    margem_superior = 100 
    posicao_esquerda = -80  

    st.markdown(
        f'''
        <img src="https://pbs.twimg.com/media/GdgsWw2XAAAQosA?format=png&name=360x360" 
        style="position: relative; top: {margem_superior}px; left: {posicao_esquerda}px; width: 25%;">
        ''',
        unsafe_allow_html=True
    )

with col2:
    outros_participantes = dados_usuarios_totais.nlargest(len(dados_usuarios_totais), "Quantidade").iloc[3:]

    if not outros_participantes.empty:
        outros_participantes = outros_participantes.reset_index(drop=True)
        outros_participantes.index = outros_participantes.index + 4

        tabela_formatada = outros_participantes[["Nome de Usuario", "Quantidade"]]
        tabela_formatada.columns = ["Usuário", "Resíduos Reciclados"]

        st.markdown(
            """
            <style>
                .stTable {
                    background-color: white;
                    border-radius: 10px;
                    padding: 10px;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                    margin-top: 140px;

                }
                .stTable th {
                    font-weight: bold;
                    color: #000;
                    text-align: center;
                    background-color: transparent;
                }
                .stTable td {
                    padding: 8px;
                    text-align: left;
                    color: #739072;
                    font-weight: bold;
                }
                .stTable tr:nth-child(odd) td {
                    background-color: transparent;
                }
                .stTable tr:nth-child(even) td {
                    background-color: #f9f9f9;
                }
            </style>
            """,
            unsafe_allow_html=True
        )

        st.table(tabela_formatada)
    else:
        st.markdown("<p class='container'>Não há outros participantes no ranking.</p>", unsafe_allow_html=True)
