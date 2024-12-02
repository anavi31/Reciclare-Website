import streamlit as st

st.set_page_config(page_title="Ranking de Reciclagem", layout="wide")

with open("ranking.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("<h1>Pódium Ranking</h1>", unsafe_allow_html=True)
st.markdown("""
<div class="ranking">
    <div class="podium">
        <div class="second">
            <div>Joana Nunes</div>
            <div>22 Reciclados</div>
        </div>
        <div class="first">
            <div>Antonio Lima</div>
            <div>24 Reciclados</div>
        </div>
        <div class="third">
            <div>Valdilene Carvalho</div>
            <div>21 Reciclados</div>
        </div>
    </div>
    <div class="list">
        <table>
            <tr><th>Rank</th><th>Usuário</th><th>Reciclados</th></tr>
            <tr><td>4</td><td>Rafael Pereira</td><td>20</td></tr>
            <tr><td>5</td><td>Larissa Santos</td><td>19</td></tr>
            <tr><td>6</td><td>Gabrielly Tavares</td><td>16</td></tr>
            <tr><td>7</td><td>Renan Matos</td><td>12</td></tr>
            <tr><td>8</td><td>Hugo Souza</td><td>8</td></tr>
            <tr><td>9</td><td>Jessica Silva</td><td>5</td></tr>
            <tr><td>10</td><td>Fernando Lima</td><td>3</td></tr>
        </table>
    </div>
</div>
""", unsafe_allow_html=True)
