# Modelo Vista Controlador usando Streamlit para el Chatbot NIST

import openai
import streamlit as st
from streamlit_chat import message

# Pedimos la API_KEY de OpenAI
if not st.session_state.get('api_key'):
    openai.api_key = st.text_input('Introduce tu clave API de OpenAI: ', key='api')
    if openai.api_key:
        st.session_state['api_key'] = openai.api_key
else:
    st.write('✅ API proporcionada')

# Condicionar chatbot a que sea un asistente NIST
contexto=[{'role': 'system', 
           'content': 'Eres el asistente de chat de NIST (Instituto Nacional de Estándares y Tecnología de los Estados Unidos por sus siglas en ingles). Tu función es ayudar a los usuarios a obtener información sobre las normas y guías de NIST. Debes responder preguntas y proporcionar información precisa y actualizada sobre las publicaciones y actividades de NIST. Tu objetivo es ayudar a los usuarios a comprender mejor cómo NIST puede ayudarles en sus necesidades de seguridad cibernética y tecnología'}]

# Título de la app y mensaje de bienvenida
st.title('🤖 Chatbot NIST')
st.write('''_Hola! Bienvenido al chat de NIST. Estoy aquí para ayudarte a obtener información sobre las normas y guías de NIST (Instituto Nacional de Estándares y Tecnología de los Estados Unidos por sus siglas en ingles)._''')
st.balloons() # Animación de globos

# Verificar si las variables de sesión existen que guardan el historial de la conversación
if 'generated' not in st.session_state:
    st.session_state.generated = []
if 'past' not in st.session_state:
    st.session_state.past = []


# Mensaje inicial, input del usuario
contenido = st.text_input('Escribe tu pregunta:', key='input')

# Historial de la charla
contexto.append({'role':'user', 'content': contenido})
# Obtener respuesta de ChatGPT-3 - NIST
respuesta = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=contexto)
# Guardamos la respuesta simplificada
respuesta_contexto= respuesta.choices[0].message.content # type: ignore
# Mantener el contexto en la conversacion para que siempre sepa todo lo que se ha dicho
contexto.append({'role':'assistant', 'content': respuesta_contexto})

st.session_state.past.append(contenido) # Imprimimos la pregunta del usuario
st.session_state.generated.append(respuesta_contexto) # Imprimimos la respuesta del chatbot

# Mantenemos el historial de la conversación en pantalla
if st.session_state.generated:
    for i in range(len(st.session_state.generated)-1,-1,-1):
        message(st.session_state.generated[i], key=str(i))
        message(st.session_state.past[i], is_user=True, key=str(i)+'_user')