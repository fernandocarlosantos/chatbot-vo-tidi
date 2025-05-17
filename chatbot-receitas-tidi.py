import os

from google.genai import types
from google.colab import userdata
from google import genai

os.environ['GOOGLE_API_KEY'] = userdata.get('GOOGLE_API_KEY')

client = genai.Client()

modelo = "gemini-2.0-flash"

chat_config = types.GenerateContentConfig(system_instruction = "Você é um assistente pessoal focado em receitas e você sempre responde como se fosse uma vovô amorosa,")

chat = client.chats.create(model=modelo, config=chat_config)

mensagem_apresentacao = "Olá, meu querido(a)! Que bom te ver por aqui, meu nome é Vó Tidi. Estou pronta para te ajudar com todas as suas dúvidas sobre receitas deliciosas."
print(mensagem_apresentacao)
print("\n")

prompt = input("O que você gostaria de aprender hoje?: ")

while prompt != "fim":
  resposta = chat.send_message(prompt)
  print("Resposta: ", resposta.text)
  print("\n")
  prompt = input("O que você gostaria de aprender hoje?: ")
