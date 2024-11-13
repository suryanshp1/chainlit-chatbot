from openai import OpenAI
from dotenv import load_dotenv
from src.prompt import system_instruction
import os

load_dotenv()

GROQ_API_TOKEN = os.getenv('GROQ_API_KEY')

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=GROQ_API_TOKEN
)


messages = [
    {
        "role": "system",
        "content": system_instruction
    }
]

def ask_order(messages, model="llama-3.1-70b-versatile", temperature = 0):
    response = client.chat.completions.create(
        model=model,
        messages = messages,
        temperature = temperature 
    )

    return response.choices[0].message.content