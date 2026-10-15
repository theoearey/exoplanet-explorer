# Importar OpenAI
from openai import OpenAI

# Crear cliente
client = OpenAI()

# Hacer una llamada simple
response = client.responses.create(model="gpt-5.6",input="Explica qué es un exoplaneta en una frase.")

# Mostrar respuesta
print(response.output_text)