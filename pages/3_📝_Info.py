import streamlit as st

# st.write("Hello World")

st.sidebar.success("Select a page above.")

# Inserta las imágenes en el título
st.header('Información del Proyecto')
st.markdown(''' El proyecto Queria fue diseñado como una DEMO para una formación centrada en analisis de datos.

No se trata de una aplicación con fines comerciales, sino más bien divulgativa, el código esta público
en mi repositorio de Github para que cualquiera que lo desee pueda replicarlo.

La API utilizada es la de OpenAI para hacer la llamada al LLM.

Confío en que hayas probado la funcionalidad y te haya gustado el proyecto, ¡Muchas gracias por haber llegado hasta aquí!
'''#, unsafe_allow_html=True
)

path_olex = "https://www.linkedin.com/in/olexandrazaporozhets/"
path_unicorn = "https://www.linkedin.com/school/unicornacademyes/"
path_nacho = "https://www.linkedin.com/in/nachomart6/"

st.header('Agradecimientos')
st.markdown(f'''En primer lugar, agradecer a mi compañera [Olex]({path_olex}) por su gran labor en las distintas tareas
(Recolección del dato, BBDD, analítica avanzada...) realizadas y sobretodo por su paciencia conmigo durante todo el proyecto (que no ha sido poca ;).
            
También agradecer a [UnicornAcademy]({path_unicorn}) por la oportunidad de realizar este proyecto dentro de su programa formativo,
por la formación ofrecida, el feedback y por todo el apoyo realizado!

***Y por supuesto gracias a ti, por haber visto la aplicación, espero que te haya gustado.***

Para cualquier consulta profesional, nos vemos por [Linkedin]({path_nacho}). Un saludo! 👋🏾)

'''#,  unsafe_allow_html=True
)
