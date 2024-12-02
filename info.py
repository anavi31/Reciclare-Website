import streamlit as st

st.set_page_config(
    page_title="Reciclare",
    page_icon="planta.png",
    layout="wide"
)

with open("info.css") as css_file:
    st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

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

st.markdown("""
    <div class="container">
        <p class="slogan">Reciclare: Pequenas ações, grandes mudanças. Juntos, por um futuro sustentável.</p>
        <h1 class="titulo">Reciclare: Transformando o hoje para preservar o amanhã.</h1>
        <h2 class="subtitulo">Como descartar corretamente os seus resíduos:</h2>
        <p class="topicos">O que é reciclável?</p>
        <p class="texto">
            É reciclável todo o resíduo descartado que constitui interesse de transformação de partes ou o seu todo. Esses materiais poderão retornar à cadeia produtiva para virar o mesmo produto ou produtos diferentes dos originais.
            Por exemplo: Folhas e aparas de papel, jornais, revistas, caixas, papelão, PET, recipientes de limpeza, latas de cerveja e refrigerante, canos, esquadrias, arame, todos os produtos eletroeletrônicos e seus componentes, embalagens em geral e outros.
        </p>
        <p class="topicos">Como separar o lixo doméstico?</p>
        <p class="texto">
            Não misture recicláveis com orgânicos - sobras de alimentos, cascas de frutas e legumes. Coloque plásticos, vidros, metais e papéis em sacos separados.<br><br>
            Lave as embalagens do tipo longa vida, latas, garrafas e frascos de vidro e plástico. Seque-os antes de depositar nos coletores.<br><br>
            Papéis devem estar secos. Podem ser dobrados, mas não amassados.<br><br>
            Embrulhe vidros quebrados e outros materiais cortantes em papel grosso (do tipo jornal) ou colocados em uma caixa para evitar acidentes. Garrafas e frascos não devem ser misturados com os vidros planos.
        </p>
        <p class="topicos">O que não vai para o lixo reciclável?</p>
        <p class="texto">
            Papel-carbono, etiqueta adesiva, fita crepe, guardanapos, fotografias, filtro de cigarros, papéis sujos, papéis sanitários, copos de papel. Cabos de panela e tomadas. Clipes, grampos, esponjas de aço, canos. Espelhos, cristais, cerâmicas, porcelana.<br><br>
            Pilhas e baterias de celular devem ser devolvidas aos fabricantes ou depositadas em coletores específicos.<br><br>
            E as embalagens mistas: feitas de plástico e metal, metal e vidro e papel e metal?<br>
            Nas compras, prefira embalagens mais simples. Mas, se não tiver opção, desmonte-a separando as partes de metal, plástico e vidro e deposite-as nos coletores apropriados. No caso de cartelas de comprimidos, é difícil desgrudar o plástico do papel metalizado, então descarte-as junto com os plásticos. Faça o mesmo com bandejas de isopor, que viram matéria-prima para blocos da construção civil.
        </p>
        <p class="topicos">Outras dicas:</p>
        <p class="texto">
            Papéis: todos os tipos são recicláveis, inclusive caixas do tipo longa-vida e de papelão. Não recicle papel com material orgânico, como caixas de pizza cheias de gordura, pontas de cigarro, fitas adesivas, fotografias, papéis sanitários e papel-carbono.<br><br>
            Plásticos: 90% do lixo produzido no mundo são à base de plástico. Por isso, esse material merece uma atenção especial. Recicle sacos de supermercados, garrafas de refrigerante (pet), tampinhas e até brinquedos quebrados.<br><br>
            Vidros: quando limpos e secos, todos são recicláveis, exceto lâmpadas, cristais, espelhos, vidros de automóveis ou temperados, cerâmica e porcelana.<br><br>
            Metais: além de todos os tipos de latas de alumínio, é possível reciclar tampinhas, pregos e parafusos. Atenção: clipes, grampos, canos e esponjas de aço devem ficar de fora.<br><br>
            Isopor: Ao contrário do que muita gente pensa, o isopor é reciclável. No entanto, esse processo não é economicamente viável. Por isso, é importante usar o isopor de diversas formas e evitar ao máximo o seu desperdício. Quando tiver que jogar fora, coloque na lata de plásticos. Algumas empresas transformam em matéria-prima para blocos de construção civil.
        </p>
        <p class="topicos">Curiosidades interessantes:</p>
        <p class="texto">
            A reciclagem de uma única lata de alumínio economiza energia suficiente para manter uma TV ligada durante três horas.<br><br>
            Cerca de 100 mil pessoas no Brasil vivem exclusivamente de coletar latas de alumínio e recebem em média três salários mínimos mensais, segundo a Associação Brasileira do Alumínio.<br><br>
            Uma tonelada de papel reciclado economiza 10mil litros de água e evita o corte de 17 árvores adultas.<br><br>
            Cada 100 toneladas de plástico reciclado economizam 1 tonelada de petróleo.<br><br>
            Um quilo de vidro quebrado faz 1kg de vidro novo e pode ser infinitamente reciclado.<br><br>
            O lacre da latinha não vale mais e não deve ser vendido separadamente. As empresas reciclam a lata com ou sem o lacre. Isso porque o anel é pequeno e pode se perder durante o transporte.<br><br>
            Para produzir 1 tonelada de papel é preciso 100 mil litros de água e 5 mil KW de energia. Para produzir a mesma quantidade de papel reciclado, são usados apenas 2 mil litros de água e 50% da energia.<br><br>
            Cada 100 toneladas de plástico economizam uma tonelada de petróleo.
            O vidro pode ser infinitamente reciclado.
        </p>
        <p class="slogan">Fonte: RIBEIRO, Rafaela. Como e porquê separar o lixo? Ministério do Meio Ambiente e Mudança do Clima, Gov.com.br.
    </div>
""", unsafe_allow_html=True)