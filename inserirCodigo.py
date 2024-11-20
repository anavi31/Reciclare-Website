import streamlit as st

def add_css(inserirCodigo):
    with open(inserirCodigo) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(
    page_title="Verificar E-mail",
    page_icon="📧",
    layout="wide"
)

add_css("inserirCodigo.css")

col1, col2 = st.columns([2, 3])

with col1:
    st.markdown("<h1>Verificar E-mail</h1>", unsafe_allow_html=True)
    st.markdown(
        '<p class="instruction">Nós enviamos um código de 4 dígitos para o seu endereço de e-mail.</p>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="code-inputs">
            <input type="text" id="digit1" maxlength="1" oninput="moveFocus(1)" onkeydown="validateNumber(event)">
            <input type="text" id="digit2" maxlength="1" oninput="moveFocus(2)" onkeydown="validateNumber(event)">
            <input type="text" id="digit3" maxlength="1" oninput="moveFocus(3)" onkeydown="validateNumber(event)">
            <input type="text" id="digit4" maxlength="1" oninput="moveFocus(4)" onkeydown="validateNumber(event)">
        </div>
        <script>
            function validateNumber(event) {
                const allowedKeys = ["Backspace", "ArrowLeft", "ArrowRight", "Tab"];
                if (!/[0-9]/.test(event.key) && !allowedKeys.includes(event.key)) {
                    event.preventDefault();
                }
            }

            function moveFocus(current) {
                const currentInput = document.getElementById(`digit${current}`);
                const nextInput = document.getElementById(`digit${current + 1}`);
                if (currentInput.value && nextInput) {
                    nextInput.focus();
                }
            }
        </script>
        """,
        unsafe_allow_html=True,
    )

    col_reenviar, col_confirmar = st.columns([1, 1])
    with col_reenviar:
        st.button("Reenviar Código")
    with col_confirmar:
        if st.button("Confirmar"):
            st.success("Código verificado com sucesso!")

    st.markdown(
        '<img src="mascote.png" class="mascote">',
        unsafe_allow_html=True,
    )

with col2:
    st.markdown('<div class="right-section">Reciclare</div>',
                unsafe_allow_html=True)
