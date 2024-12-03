import csv
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Questionário dos Hábitos de descarte", page_icon="🌱", layout="centered")

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

if "usuario" not in st.session_state:
    usuario = st.text_input("Por favor, insira seu nome de usuário:")
    if usuario:
        st.session_state.usuario = usuario
    else:
        st.stop()

if "pagina_atual" not in st.session_state:
    st.session_state.pagina_atual = 0
    st.session_state.respostas = []

pagina = st.session_state.pagina_atual

def atualizar_ranking(usuario, ranking):
    df = pd.read_csv('dados_usuarios.csv')
    
    if usuario in df['Nome de Usuario'].values:
        df.loc[df['Nome de Usuario'] == usuario, 'Ranking'] = ranking
        df.to_csv('dados_usuarios.csv', index=False)
        st.success(f"Ranking '{ranking}' salvo para o usuário {usuario}!")
    else:
        st.error("Usuário não encontrado. Por favor, verifique o nome.")

st.markdown('<div class="footer"></div>', unsafe_allow_html=True)

if pagina < len(perguntas):
    st.markdown(f'<div class="title">Pergunta {pagina + 1} de {len(perguntas)}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="question">{perguntas[pagina]}</div>', unsafe_allow_html=True)

    resposta = st.radio("", opcoes, key=f"resposta_{pagina}")

    if st.button("Continuar"):
        st.session_state.respostas.append(resposta)
        st.session_state.pagina_atual += 1

else:
    peso = {"Sim": 1, "Um pouco": 0.75, "Não sei dizer": 0.5, "Não muito": 0.25, "Não": 0}
    total = sum([peso[r] for r in st.session_state.respostas])
    percentual = (total / len(perguntas)) * 100

    if percentual >= 76:
        ranking = "Gardênia"
        mensagem = "Parabéns! Você é um verdadeiro Reciclinho! Seu comportamento de descarte é exemplar. Continue assim, o meio ambiente agradece!"
    elif percentual >= 51:
        ranking = "Crisântemo"
        mensagem = "Você está quase lá! Falta pouco para se tornar um Reciclinho. Pequenos ajustes nos seus hábitos de descarte podem fazer uma grande diferença. Vamos juntos melhorar!"
    elif percentual >= 26:
        ranking = "Alstroeméria"
        mensagem = "Atenção! Há espaço para melhorias nos seus hábitos de descarte. Você está no caminho certo, mas ainda pode fazer mais. Que tal rever como descartar alguns materiais?"
    else:
        ranking = "Gloxínia"
        mensagem = "Ops! Parece que os seus hábitos de descarte precisam de bastante atenção. Vamos começar com pequenas mudanças e aprender juntos como melhorar o cuidado com o meio ambiente!"
    
    st.markdown("""
    <header class="header">
        <div class="logo-container">
            <img src="https://pbs.twimg.com/media/GdKDgEnXYAAKJ7o?format=webp&name=tiny" class="logo">
            <span class="site-name">Reciclare</span>
        </div>
    </header>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <h1>Resultados</h1>
    <div class="texto">
        <h2>O nosso sistema de ranking de reciclagem foi criado para reconhecer e incentivar hábitos sustentáveis, comparando suas ações com outros participantes da comunidade.</h2>
        <h2>Com base na sua dedicação ao descarte correto e na quantidade de resíduos reciclados, você foi classificado no Ranking <strong>{ranking}</strong>!</h2>
        <h2>{mensagem}</h2>
        <h2>Continue participando e avançando em seus hábitos de reciclagem para subir ainda mais nos nossos rankings. O planeta e a comunidade agradecem! 🌱</h2>
    </div>
    """, unsafe_allow_html=True)

    if "usuario" in st.session_state:
        atualizar_ranking(st.session_state.usuario, ranking)

    st.markdown("""
                <a href="http://localhost:8503/">
                    <button style="
                        background-color: #7a9f84;
                        color: white;
                        padding: 10px 24px;
                        border: 0;
                        cursor: pointer;
                        font-size: 16px;
                        border-radius: 5px;
                        margin-top: 30px;
                        margin-left: 270px">
                        Fazer Login
                    </button>
                </a>
            """, unsafe_allow_html=True)
