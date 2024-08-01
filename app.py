


import utils
import os
from ..queria_app import env
# import env
import streamlit as st

from openai import OpenAI
from PIL import Image



st.set_page_config(
    page_title="QuerIA",
    page_icon="📊"
)

tabs = st.tabs(["GPT", "Dashboard"])

with tabs[0]: 
    st.sidebar.success("Select a demo above.")

    # Upload avatar images
    avatar_asistente = Image.open("images/icon_bot.png")
    avatar_usuario = Image.open("images/icon_developer.png")


    # Inserta las imágenes en el título
    st.markdown(f'<h1>Bienvenido a Quer<span style="color:dodgerblue">IA</span>!', unsafe_allow_html=True)
    st.markdown(f'<h3>¡Consulta a la BBDD unicamente mediante un prompt!</h3>', unsafe_allow_html=True)
    st.markdown('''Por favor, hay una serie de reglas que debes cumplir:
                
    1. Trata siempre de generar oraciones completas, nada de Hola, adios, si o no...
    2. La consulta que realices tiene que estar planteada para ser traducida a SQL.
    3. Los prompts tienen que centrarse en la temática del GPT y no en temas distintos a los destinados.
            
    Si realizais todos los pasos, podreís consultar de manera éxitosa a la BBDD, ¡muchas gracias por tu comprensión!''')

    # os.environ["OPENAI_API_KEY"] = str(os.getenv('QUERIA_KEY'))
    # api_key = str(os.getenv('KEY_QUERIA'))
    api_key = str(env.KEY_QUERIA)

    client = OpenAI(api_key=api_key)

    template = """

    Eres un agente de SQL, recibiendo una respuesta tu objetivo es dejarla tal cual y enviarla de vuelta.

    Si viene en formato markdown, mantienes el formato markdown.

    El objetivo es que simplemente repliques el contenido que te viene.

    No puedes realizar ninguna otra operación que la mencionada.

    Aquí tienes la respuesta a replicar:

    {respuesta}

    """



    # Me crea una variable MODELO, que ahora mismo no necesito, porque mi modelo es otro, al que llama´re de utils
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = 'gpt-3.5-turbo'

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"], avatar=message['avatar']):
            st.markdown(message["content"])



    # def response_generator(prompt):
    #     respuesta = utils.talk_to_sql(prompt)
        
    #     for word in respuesta.split():
    #         yield word + " "
    #         time.sleep(0.01)



    if prompt := st.chat_input("Tu mejor prompt"):
        
        # Display user message in chat message container
        with st.chat_message("user", avatar=avatar_usuario):
            st.markdown(prompt)
            
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt, 'avatar': avatar_usuario})

        with st.chat_message("assistant", avatar=avatar_asistente):
            respuesta = utils.talk_to_sql(prompt)
            st.session_state.messages.append({"role": "system", "content": respuesta, 'avatar': avatar_asistente})
            mensajes  = [{"role" : "system", "content": template.format(respuesta=respuesta)}]
            # history = [{"role": m["role"], "content": m["content"]}
            #         for m in st.session_state.messages]
            stream = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages= mensajes, #+ history,
                stream=True,
            )

            # response = st.write_stream(response_generator(prompt))
            response = st.write_stream(stream)


with tabs[1]:
     st.write("Hello World")
















