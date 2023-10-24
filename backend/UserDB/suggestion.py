import os
import openai
OPENAI_API = os.environ.get('OPENAI_API')
openai.api_key = OPENAI_API

def generate_suggestion(data: list[float])-> str:
    tuition = data[0]
    rent = data[1]
    grocery = data[2]
    eating_out = data[3]
    transit = data[4]
    boursaries = data[5]
    loans = data[6]
    income = data[7]

    text_prompt = "" + tuition + "" + rent + "" + grocery + "" + eating_out + "" + transit + "" + boursaries + "" + loans + "" + income + ""

    chatgpt_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text_prompt}],
        temperature=0.7,
        max_tokens=2000,
        top_p=0.95)
    
    response = chatgpt_response['choices'][0]['message']['content'].strip()

    return response
