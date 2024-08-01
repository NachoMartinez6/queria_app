

# Importamos librerias

import os
import warnings
# import env
from ..env import env

from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain_experimental.sql import SQLDatabaseChain

warnings.filterwarnings(
    'ignore',
    '.*',
    UserWarning,
    'warnings_filter',
)


# Cargamos la variable de entorno
# os.environ["OPENAI_API_KEY"] = env.QUERIA_KEY
os.environ["OPENAI_API_KEY"] = str(env.KEY_QUERIA)


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


# respuesta = talk_to_sql("Cual es el numero de registros totales para la tabla de energy_dataset?")
# print(respuesta)





