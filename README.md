# Chatbot NIST

Este es un chatbot de NIST (Instituto Nacional de Estándares y Tecnología de los Estados Unidos) construido con Streamlit y OpenAI. Su función es ayudar a los usuarios a obtener información sobre las normas y guías de NIST. El chatbot responde preguntas y proporciona información precisa y actualizada sobre las publicaciones y actividades de NIST.

### Instalación
Para ejecutar este chatbot, necesitarás tener Python 3.x instalado en tu computadora. También necesitarás instalar las siguientes librerías incluidas en el archivo requirements.txt:

<code>pip install openai</code>

<code>pip install streamlit</code>

<code>pip install streamlit_chat</code>

o puedes instalarlas todas a la vez con el siguiente comando:

<code>pip install -r requirements.txt </code>

Además, necesitarás una clave [API de OpenAI](https://platform.openai.com/account/api-keys) para poder utilizar su modelo GPT-3.5-turbo. Puedes obtener una clave API registrándote en OpenAI.

### Configuración
Antes de ejecutar el chatbot, asegúrate de agregar tu clave API de OpenAI al archivo config.py:

<code>API_KEY = "TU_CLAVE_API_AQUÍ"</code>

### Ejecución
Para ejecutar el chatbot, simplemente navega al directorio donde se encuentra el archivo app.py y ejecuta el siguiente comando:

<code>streamlit run Chatbot-NIST.py</code>

Esto iniciará la aplicación en tu navegador web predeterminado.
### Uso
Para usar el chatbot, simplemente escribe tu pregunta en el cuadro de texto y presiona enter. El chatbot responderá con información relevante sobre las normas y guías de NIST.

### Demo
Puedes probar el chatbot en el siguiente enlace: https://gilberto-xyz-chatbot-nist-chatbot-nist-9puad3.streamlit.app/
### Documentacion
[Codigo explicado](https://gilbertscript.notion.site/MVC-Chatbot-ff152eef008c49fb87c7ec5b60ea3a21)

[Video Demostracion](https://drive.google.com/file/d/1fSTI03X2bTnaLjnSUCC963YdVI95DAVK/view?usp=sharing)
