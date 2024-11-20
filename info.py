import streamlit as st

# Configurações gerais
st.set_page_config(page_title="Informações sobre Reciclagem", layout="wide")

# Estilo CSS
with open("info.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Conteúdo
st.markdown("<h1>Reciclare: Transformando o hoje para preservar o amanhã.</h1>", unsafe_allow_html=True)
st.markdown("<h2>Como descartar corretamente os seus resíduos:</h2>", unsafe_allow_html=True)
st.markdown("""
<p>
Para descartar corretamente seus resíduos, comece separando os orgânicos, como restos de comida e folhas, que devem ser destinados à compostagem ou a lixeiras específicas, ajudando a produzir adubo.
Materiais recicláveis, como plásticos, vidros, metais e papéis, precisam ser limpos e separados antes de serem colocados em lixeiras apropriadas para reciclagem.
Resíduos perigosos, como pilhas, baterias, lâmpadas e medicamentos, devem ser descartados em pontos de coleta específicos, disponíveis em lojas e farmácias.
Itens não recicláveis, como fraldas, absorventes e esponjas, devem ir para o lixo comum. Ao seguir essas orientações, você contribui para a redução do impacto ambiental e promove um descarte mais sustentável.
</p>
""", unsafe_allow_html=True)
