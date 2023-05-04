import openai  
import config 

openai.api_key = config.API_KEY

response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo', 
    messages=[{'role': 'user', 'content': 'Por que escribimos hola mundo?'}])

print(response)