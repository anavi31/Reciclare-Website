import csv
import streamlit as st

st.set_page_config(page_title="Questionário de Descarte", page_icon="🌱", layout="centered")

def load_css_from_file(questionario):
    with open(questionario) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css_from_file("questionario.css")

perguntas = [
    "Você separa os materiais recicláveis (plástico, vidro, metal) dos resíduos orgânicos em casa?",
    "Você lava os recipientes de plástico, vidro ou metal antes de descartá-los?",
    "Você leva seus resíduos recicláveis a um ponto de coleta seletiva?",
    "Você sabe quais materiais são recicláveis na sua cidade?",
    "Você procura reduzir a quantidade de resíduos que gera?",
    "Você reutiliza materiais como garrafas ou sacolas antes de descartá-los?",
    "Você costuma ler as instruções de reciclagem nas embalagens dos produtos?",
    "Você evita comprar produtos com embalagens não recicláveis?",
    "Você utiliza sacolas reutilizáveis ao invés de sacolas plásticas?",
    "Você se informa sobre os dias de coleta seletiva no seu bairro?"
]


opcoes = ["Sim", "Um pouco", "Não sei dizer", "Não muito", "Não"]

if "pagina_atual" not in st.session_state:
    st.session_state.pagina_atual = 0
    st.session_state.respostas = []

pagina = st.session_state.pagina_atual

if pagina < len(perguntas):
    # Descrição fixa no canto superior esquerdo
    st.markdown('<div class="description">Responda um pequeno questionário sobre seus atuais hábitos de descarte para que possamos personalizar sua experiência.</div>', unsafe_allow_html=True)
    
    # Título com número da pergunta
    st.markdown(f'<div class="title">Pergunta {pagina + 1}</div>', unsafe_allow_html=True)
    
    # Texto da pergunta
    st.markdown(f'<div class="question">{perguntas[pagina]}</div>', unsafe_allow_html=True)

    # Respostas com botões coloridos horizontalmente
    resposta = st.radio("", opcoes, key=f"resposta_{pagina}")

    st.markdown(
    """
      <div class="footer">
            <div class="button-container">
                 <!-- O botão do Streamlit será renderizado aqui -->
            </div>
        </div>
    """,
    unsafe_allow_html=True,
    )

    st.markdown(
    """
    <style>
            .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            height: 100px;
            background-color: #7a9f84;
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 10;
        }

        .button-container {
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .stButton button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        .stButton button:hover {
            background-color: #45a049;
        }
    </style>
    """,
    unsafe_allow_html=True,
    )

    with st.container():
        col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        if st.button("Continuar"):
            st.session_state["next_question"] = True  # Substituir por lógica de navegação


else:
    # Exibição dos resultados
    st.markdown('<div class="title">Resultados do Questionário</div>', unsafe_allow_html=True)

    peso = {"Sim": 1, "Um pouco": 0.75, "Não sei dizer": 0.5, "Não muito": 0.25, "Não": 0}
    total = sum([peso[r] for r in st.session_state.respostas])
    percentual = (total / len(perguntas)) * 100

    st.markdown(f"""
    <div class="result">
        <p>Sua pontuação foi: <strong>{percentual:.2f}%</strong></p>
    </div>
    """, unsafe_allow_html=True)

    with open("dados_usuarios.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([percentual])

    if st.button("Reiniciar"):
        st.session_state.pagina_atual = 0
        st.session_state.respostas = []
