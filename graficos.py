import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Monitoramento de Reciclagem", layout="wide")

with open("graficos.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""
<header class="header">
    <div class="logo-container">
        <img src="https://pbs.twimg.com/media/GdKDgEnXYAAKJ7o?format=webp&name=tiny" class="logo">
        <span class="site-name">Reciclare</span>
    </div>
    <div class="header-button-container">
        <a href="">Tela Inicial</a>
        <a href="">Informações Sobre Reciclare</a>
        <a href="">Ranking</a>
    </div>
</header>
""", unsafe_allow_html=True)

st.markdown("<h1>Monitoramento de Reciclagem</h1>", unsafe_allow_html=True)
st.markdown("<h2>Resultados em Gráficos</h2>", unsafe_allow_html=True)

@st.cache_data
def load_data():
    return pd.read_csv("residuos.csv")

df = load_data()

st.markdown("<h3>Selecione um intervalo de datas:</h3>", unsafe_allow_html=True)
date_column = 'Data'  
df[date_column] = pd.to_datetime(df[date_column])  

start_date = st.date_input("Data inicial", min_value=df[date_column].min(), max_value=df[date_column].max())
end_date = st.date_input("Data final", min_value=df[date_column].min(), max_value=df[date_column].max())

if start_date and end_date:
    filtered_df = df[(df[date_column] >= pd.Timestamp(start_date)) & (df[date_column] <= pd.Timestamp(end_date))]
else:
    filtered_df = df

if filtered_df.empty:
    st.warning("Não há dados para o intervalo selecionado.")
else:
    st.markdown("<h4>Gráfico de Resíduos</h4>", unsafe_allow_html=True)
    custom_colors = ['#739072', '#739072', '#739072', '#739072', '#739072']
    fig = px.bar(
        filtered_df,
        x='Tipo de Resíduo',
        y='Quantidade',
        color='Tipo de Resíduo',
        labels={'Tipo de Resíduo': 'Tipo de Resíduo', 'Quantidade': 'Quantidade Reciclada'},
        title="Quantidade e Tipo de Resíduos Descartados",
        color_discrete_sequence=custom_colors
    )
    st.plotly_chart(fig, use_container_width=True)