import openai  
import config 

openai.api_key = config.API_KEY

# Mensaje de bienvenida
print("¡Hola! Bienvenido al chat de NIST. Estoy aquí para ayudarte a obtener información sobre las normas y guías de NIST. \n Si deseas salir del chat, escribe 'adios' y presiona enter.")
# Condicionar chatbot a que sea un asistente NIST
contexto=[{'role': 'system', 
           'content': 'Eres el asistente de chat de NIST (Instituto Nacional de Estándares y Tecnología de los Estados Unidos por sus siglas en ingles). Tu función es ayudar a los usuarios a obtener información sobre las normas y guías de NIST. Debes responder preguntas y proporcionar información precisa y actualizada sobre las publicaciones y actividades de NIST. Tu objetivo es ayudar a los usuarios a comprender mejor cómo NIST puede ayudarles en sus necesidades de seguridad cibernética y tecnología'}]

# Mantener la conversación en loop
while True:

    # Mensaje inicial
    contenido = input('\nEscribe tu pregunta: ')

    if contenido == 'adios':
        break
    if contenido == '' or contenido == ' ' or contenido == 'exit' or contenido == 'salir':
        print('Por favor, introduce tu consulta o pregunta en el cuadro de texto a continuación y presiona enter para enviarla. Estoy aquí para ayudarte con información sobre las normas y guías de NIST. \n Si deseas salir del chat, escribe "adios" y presiona enter.)')

    # Historial de la charla
    contexto.append({'role':'user', 'content': contenido})

    # Obtener respuesta de ChatGPT-3 - NIST
    respuesta = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=contexto)

    # Guardamos la respuesta simplificada
    respuesta_contexto= respuesta.choices[0].message.content # type: ignore

    # Mantener el contexto en la conversacion para que siempre sepa todo lo que se ha dicho
    contexto.append({'role':'assistant', 'content': respuesta_contexto})

    # Respuesta 
    print(respuesta_contexto)