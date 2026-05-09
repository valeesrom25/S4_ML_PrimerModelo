import streamlit as st
import random
import time

# Configuración de página
st.set_page_config(
    page_title="Ecuaciones de Primer Grado",
    page_icon="🧠",
    layout="centered"
)

# CSS personalizado para animaciones
st.markdown("""
<style>
.big-title {
    text-align: center;
    font-size: 45px;
    color: #4CAF50;
    animation: fadeIn 1.5s ease-in-out;
}

.question-box {
    padding: 20px;
    border-radius: 15px;
    background-color: #1e1e1e;
    text-align: center;
    font-size: 35px;
    margin-top: 20px;
    animation: slideUp 0.8s ease;
}

.correct {
    color: #00ff88;
    font-size: 28px;
    text-align: center;
    animation: pop 0.5s ease;
}

.incorrect {
    color: #ff4b4b;
    font-size: 28px;
    text-align: center;
    animation: shake 0.5s ease;
}

@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}

@keyframes slideUp {
    from {
        transform: translateY(30px);
        opacity: 0;
    }
    to {
        transform: translateY(0px);
        opacity: 1;
    }
}

@keyframes pop {
    0% {transform: scale(0.8);}
    100% {transform: scale(1);}
}

@keyframes shake {
    0% {transform: translateX(0);}
    25% {transform: translateX(-5px);}
    50% {transform: translateX(5px);}
    75% {transform: translateX(-5px);}
    100% {transform: translateX(0);}
}
</style>
""", unsafe_allow_html=True)

# Título
st.markdown('<h1 class="big-title">🧠 Resolver Ecuaciones</h1>', unsafe_allow_html=True)

# Inicializar variables de sesión
if "score" not in st.session_state:
    st.session_state.score = 0

if "equation" not in st.session_state:
    st.session_state.equation = None

if "solution" not in st.session_state:
    st.session_state.solution = None


# Función para generar ecuación
def generar_ecuacion():
    x = random.randint(-10, 10)

    a = random.randint(1, 10)
    b = random.randint(-20, 20)

    c = a * x + b

    ecuacion = f"{a}x + ({b}) = {c}"

    return ecuacion, x


# Botón para nueva ecuación
if st.button("🎲 Generar Nueva Ecuación"):

    ecuacion, solucion = generar_ecuacion()

    st.session_state.equation = ecuacion
    st.session_state.solution = solucion

# Mostrar ecuación
if st.session_state.equation:

    st.markdown(
        f'<div class="question-box">{st.session_state.equation}</div>',
        unsafe_allow_html=True
    )

    respuesta = st.number_input("Ingresa el valor de x:", step=1)

    if st.button("✅ Verificar Respuesta"):

        with st.spinner("Verificando respuesta..."):
            time.sleep(1)

        if respuesta == st.session_state.solution:

            st.session_state.score += 1

            st.balloons()

            st.markdown(
                '<p class="correct">🎉 ¡Correcto!</p>',
                unsafe_allow_html=True
            )

        else:

            st.markdown(
                f'<p class="incorrect">❌ Incorrecto. La respuesta era x = {st.session_state.solution}</p>',
                unsafe_allow_html=True
            )

# Puntaje
st.markdown("---")
st.subheader(f"🏆 Puntaje: {st.session_state.score}")
