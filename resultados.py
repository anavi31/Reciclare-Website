import streamlit as st

# Carregar estilo CSS
with open("resultados.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Layout da página
st.markdown('<div class="header">Resultados:</div>', unsafe_allow_html=True)

st.markdown("""
<div class="content">
    <p>O nosso sistema de ranking de reciclagem foi criado para reconhecer e incentivar hábitos sustentáveis, comparando suas ações com outros participantes da comunidade.</p>
    <p>Com base na sua dedicação ao descarte correto e na quantidade de resíduos reciclados, você foi classificado no <strong>Ranking Alstroemeria!</strong> Atenção, há espaço para melhorias nos seus hábitos de descarte. Você está no caminho certo, mas ainda pode fazer mais. Que tal rever como descarta alguns materiais?</p>
    <p>Como reconhecimento, seu ícone de perfil agora será personalizado com a flor Alstroemeria, representando seu excelente desempenho na reciclagem.</p>
    <p>Continue participando e avançando em seus hábitos de reciclagem para subir ainda mais nos nossos rankings. O planeta e a comunidade agradecem! 🌱</p>
</div>
""", unsafe_allow_html=True)

if st.button("DICAS"):
    st.info("Dicas para melhorar o descarte estão disponíveis!")
