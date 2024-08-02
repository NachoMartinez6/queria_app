
import warnings

from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain_experimental.sql import SQLDatabaseChain

warnings.filterwarnings(
    'ignore',
    '.*',
    UserWarning,
    'warnings_filter',
)


import os
import streamlit as st

from openai import OpenAI
from PIL import Image


################## BACKEND



os.environ["OPENAI_API_KEY"] = str(st.secrets["KEY_QUERIA"])


# Cargamos la BBDD con langchain
db = SQLDatabase.from_uri("sqlite:///queria.db")

# Creamos el LLM
llm = ChatOpenAI(temperature=0, model='gpt-3.5-turbo')

# Creamos la cadena
cadena = SQLDatabaseChain.from_llm(llm=llm, db=db, verbose=False)

# Generamos el prompt
template_prompt = """
Eres un agente SQL especializado en trabajar traduciendo consultas de usuario a lenguaje SQL y trayendo el resultado.

Dada una pregunta del usuario, quiero que realices el siguiente paso a paso:

1. Crea una consulta de sqlite3.
2. Revisa los resultados
3. Devuelve el dato que corresponda.
4. Si tienes que hacer alguna aclaración de devolver cualquier texto que sea en español

Importante: 

Si no te dan promps que puedan ser pasados a lenguaje SQL, indica que no puedes realizar una consulta SQL válida que pruebe de otra forma.
Si te piden otro tipo de información, indica que tu campo de acción se limita a trabajar con lenguaje SQL.
No pueden hacer DELETE a la tabla, ni crear tablas mediante las consultas que te pidan.
Trata siempre de trabajar tu respuesta y que sea usualmente extensa.


Consulta: {question} 


"""

def talk_to_sql(prompt):
    try:
        consulta = template_prompt.format(question=prompt)
        respuesta = cadena.invoke(consulta)
        resultado = respuesta.get('result')
    
    except:
        resultado = "No puedo realizar una consulta SQL válida con la información proporcionada. Por favor proporcione una pregunta que pueda ser traducida a una consulta SQL."
    return resultado




################## FRONTEND


st.set_page_config(
    page_title="QuerIA",
    page_icon="📊"
)


st.sidebar.success("Select a page above.")


# tabs = st.tabs(["GPT", "Dashboard"])

# with tabs[0]: 

# Upload avatar images
avatar_asistente = Image.open("images/icon_bot.png")
avatar_usuario = Image.open("images/icon_developer.png")

dashboard_path = "https://queria.streamlit.app/Dashboard"


# Inserta las imágenes en el título
st.markdown(f'<h1>Bienvenido a Quer<span style="color:dodgerblue">IA</span>!', unsafe_allow_html=True)
st.markdown(f'<h3>¡Consulta a la BBDD unicamente mediante un prompt!</h3>', unsafe_allow_html=True)

st.markdown(f'''**Contexto**: La BBDD contiene una tabla denominada energy_dataset con información de la producción, exportación de electricidad
de diferentes paises de la zona euro, más información en el [Dashboard]({dashboard_path})
''')
st.markdown(f'''Por favor, hay una serie de reglas que debes cumplir:
            
1. Trata siempre de generar oraciones completas, nada de Hola, adios, si o no...
2. La consulta que realices tiene que estar planteada para ser traducida a SQL.
3. Los prompts tienen que centrarse en la temática del GPT y no en temas distintos a los destinados.

Si realizas todos los pasos, podrás consultar de manera éxitosa a la BBDD, ¡Muchas gracias por tu comprensión!''')

# os.environ["OPENAI_API_KEY"] = str(os.getenv('QUERIA_KEY'))
# api_key = str(os.getenv('KEY_QUERIA'))
# api_key = str(env.KEY_QUERIA)
api_key = str(st.secrets["KEY_QUERIA"])
client = OpenAI(api_key=api_key)


# En el caso, de que te soliciten graficas y visualizaciones, sientete libre de realizar aquellas visualizaciones que te soliciten con la info aportada


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
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt, 'avatar': avatar_usuario})
    # Display user message in chat message container
    with st.chat_message("user", avatar=avatar_usuario):
        st.markdown(prompt)
        


    with st.chat_message("assistant", avatar=avatar_asistente):
        respuesta = talk_to_sql(prompt)
        # st.session_state.messages.append({"role": "system", "content": respuesta, 'avatar': avatar_asistente})
        mensajes  = [{"role" : "user", "content": template.format(respuesta=respuesta)}]
        # history = [{"role": m["role"], "content": m["content"]}
        #         for m in st.session_state.messages]
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages= mensajes, # + history,
            stream=True,
        )

        # response = st.write_stream(response_generator(prompt))
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "system", "content": response, 'avatar': avatar_asistente})

# with tabs[1]:
#      st.write("Hello World")
















