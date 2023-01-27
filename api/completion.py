import os
import openai
from dotenv import load_dotenv
from emoji import core

def generate_txt(prompt, temperature=0.3):
    load_dotenv()
    openai.api_key = os.getenv('API_KEY')
    
    engine = "text-davinci-003"
    max_tokens = 1000

    response = openai.Completion.create(engine=engine, prompt=prompt,temperature=temperature, max_tokens=max_tokens)
    answer = str(response.choices[0].text)
    answer = answer.replace("\n", " ")
    answer = answer.lstrip("@")
    answer = core.replace_emoji(answer, replace="")
    answer = answer.lstrip(" ")
    return answer