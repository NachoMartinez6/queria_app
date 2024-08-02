import streamlit as st

# st.write("Hello World")

# Inserta las imágenes en el título
st.markdown(f'<h2>Información del Proyecto<h2>', unsafe_allow_html=True)
st.markdown('''
El proyecto Queria fue diseñado como una DEMO para una formación centrada en analisis de datos.

No se trata de una aplicación con fines comerciales, sino más bien divulgativa, el código esta público
en mi repositorio de Github para que cualquiera que lo desee pueda replicarlo.

La API utilizada es la de OpenAI para hacer la llamada al LLM.

Confío en que hayas probado la funcionalidad y te haya gustado el proyecto, ¡Muchas gracias por haber llegado hasta aquí!
''', unsafe_allow_html=True)


st.markdown(f'<h2>Agradecimientos</h2>', unsafe_allow_html=True)
st.markdown('''En primer lugar agradecer a mi compañera [Olex]("https://www.linkedin.com/in/olexandrazaporozhets/") por su ayuda y comprensión
durante todo el proyecto.
            
También agradecer a [UnicornAcademy]("https://www.linkedin.com/school/unicornacademyes/") por la formación ofrecida, por las clases
y por todo el apoyo realizado!

Y por supuesto gracias a ti, por haber visto la aplicación, espero que os guste. Un saludo! 👋🏾)

''',  unsafe_allow_html=True)
