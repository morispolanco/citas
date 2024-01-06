import streamlit as st
import openai

# Configurar la API key de OpenAI
openai.api_key = st.text_input("Ingresa tu API key de OpenAI:")

def obtener_citas_filosofos(tema):
    # Conversación con el modelo chatgpt-3.5
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Obtener diez citas de filósofos sobre {tema}.",
        max_tokens=100,
        n=10,
        stop=None,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    # Obtener las respuestas del modelo
    citas = response.choices[0]['text'].split("\n")
    
    return citas

# Interfaz de la aplicación con Streamlit
st.title("Citas de Filósofos")
tema = st.text_input("Ingresa un tema:")

if st.button("Obtener citas"):
    if tema:
        st.info("Obteniendo citas de filósofos...")
        citas = obtener_citas_filosofos(tema)
        st.success("¡Citas obtenidas!")
        for i, cita in enumerate(citas):
            st.markdown(f"**Cita {i+1}:** {cita}")
    else:
        st.warning("Por favor, ingresa un tema.")

