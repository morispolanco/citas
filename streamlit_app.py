import streamlit as st
import openai

# Configuración de Streamlit
st.title("Generador de Citas Filosóficas")
st.write("Ingrese un tema y obtendrá diez citas de filósofos relacionadas")

# Configuración de OpenAI ChatGPT
openai.api_key = st.secrets["OPENAI_API_KEY"]
model = "gpt-3.5-turbo"

# Función para generar citas
def generar_citas(tema, num_citas):
    prompt = f"Generar {num_citas} citas de filósofos sobre '{tema}'"
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=100,
        n = num_citas,
        stop=None,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    citas = [choice['text'].strip() for choice in response['choices']]
    return citas

# Interfaz de usuario
tema = st.text_input("Ingrese un tema:")
num_citas = st.slider("Número de citas", 1, 10, 5)

if st.button("Generar Citas"):
    if tema:
        with st.spinner("Generando citas..."):
            citas = generar_citas(tema, num_citas)
        st.success("¡Citas generadas!")
        for i, cita in enumerate(citas):
            st.write(f"{i+1}. {cita}")
    else:
        st.warning("Por favor, ingrese un tema")

