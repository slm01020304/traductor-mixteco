import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="🌎 Traductor Español → Mixteco",
    page_icon="🌎",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Colores y estilo con markdown
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f5f5;
        color: #2c3e50;
        font-family: 'Arial', sans-serif;
    }
    .stButton>button {
        background-color: #16a085;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        height: 50px;
        width: 150px;
    }
    .stTextInput>div>div>input {
        height: 40px;
        font-size: 16px;
        border-radius: 8px;
        padding: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título de la app
st.title("🌎 Traductor Español → Mixteco")
st.subheader("Traductor interactivo de palabras")

# Diccionario Español → Mixteco
diccionario = {
    "hola": "ndee",
    "adiós": "ka'vi",
    "gracias": "tachi",
    "amor": "kuaa",
    "amigo": "ndee ku",
    "mujer": "ña’a",
    "hombre": "ñuu",
    "comer": "kua’a",
    "beber": "tsi’i",
    "casa": "ka’an"
}

# Entrada
palabra = st.text_input("Escribe una palabra en español:")

# Botón traducir
if st.button("Traducir"):
    if palabra:
        traduccion = diccionario.get(palabra.lower(), "Traducción no encontrada")
        st.markdown(
            f"<h2 style='color:#16a085;'>👉 {palabra} → {traduccion}</h2>", 
            unsafe_allow_html=True
        )
    else:
        st.warning("⚠️ Por favor escribe una palabra.")

# Pie de página
st.markdown(
    "<p style='color:#7f8c8d; text-align:center;'>Diccionario básico • Puedes agregar más palabras</p>",
    unsafe_allow_html=True
)
