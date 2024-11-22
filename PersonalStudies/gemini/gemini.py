import google.generativeai as genai
import os

from Scripts.prichunkpng import process


def Gemini(pergunta):
    api = os.environ["API_KEY"] = process.env.API_KEY
    genai.configure(api_key=api)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(pergunta)
    return response.text


p = input("Gemini Prompt, faça sua pergunta: ")
print(Gemini(p))