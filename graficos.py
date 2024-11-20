import streamlit as st

# Configurações gerais
st.set_page_config(page_title="Monitoramento de Reciclagem", layout="wide")

# Estilo CSS
with open("graficos.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Conteúdo
st.markdown("<h1>Monitoramento de Reciclagem</h1>", unsafe_allow_html=True)
st.markdown("<h2>Resultados em Gráficos</h2>", unsafe_allow_html=True)

st.markdown("""
<div class="grafico">
    <h3>Produtos reciclados</h3>
    <div class="circle-chart">100% de aproveitamento</div>
    <button>Selecionar Data</button>
</div>
""", unsafe_allow_html=True)
