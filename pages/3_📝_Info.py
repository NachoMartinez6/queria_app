import streamlit as st

# st.write("Hello World")

st.sidebar.success("Select a page above.")

path_repo = "https://github.com/NachoMartinez6"

# Inserta las imágenes en el título
st.header('Información del Proyecto')
st.markdown(f''' El proyecto Queria fue diseñado como una **DEMO** para una formación centrada en analisis de datos.

No se trata de una aplicación con fines comerciales, sino más bien divulgativa, el código esta público
en mi [repositorio de Github]({path_repo}) para que cualquiera que lo desee pueda replicarlo.

La API utilizada es la de OpenAI para hacer la llamada al LLM.

***Confío en que hayas probado la funcionalidad y te haya gustado el proyecto, ¡Muchas gracias por haber llegado hasta aquí!***
'''#, unsafe_allow_html=True
)

