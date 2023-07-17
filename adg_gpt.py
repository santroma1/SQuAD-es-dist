import json
import requests
from tqdm import tqdm

import openai
import dotenv
import os
import jsonlines as jsl
import time


SEP = "[SEP]"
CLS = "[CLS]"

if __name__ == '__main__':
    dotenv.load_dotenv()

    openai.api_key = os.getenv('DG_GPT_KEY')

    default_prompt = "La generación de distractores en el contexto de preguntas de opción múltiple es una tarea que con un texto, una pregunta, y una respuesta correcta, se busca generar las respuestas distractoras. Las respuestas distractoras son respuestas incorrectas a una pregunta, pero que tienen la capacidad de confundir a un estudiante, y que son sintácticamente similares a la respuesta correcta. Las respuestas distractoras deben ser gramáticamente similares a la respuesta correcta, por ejemplo, si la respuesta correcta empieza con una letra minúscula, las respuestas distractoras también deben empezar con una letra minúscula. Las respuestas distractoras serán mejores también si pertenecen al mismo grupo semántico que la respuesta correcta. Voy a poner un texto, una pregunta, y la respuesta correcta, y tu tarea es generar 3 respuestas distractoras. Recuerda que debes generar buenas respuestas distractoras como las describí. Es muy importante que las respuestas distractoras deben ser extraídas del texto, y que las respuestas distractoras no sean explícitamente la respuesta correcta. Si haces las respuestas distractoras similares entre ellas, pero diferentes a la respuesta correcta, un estudiante podría intuir cuál es la respuesta correcta, al ver que hay una respuesta que es diferente en su forma a las demás."

    # current_file = "dev.json"
    current_file = "test.json"
    path = os.path.join("data", current_file)
    f = open(path)
    data = json.load(f)
    data = data["data"]
    # data = data[:5]
    temp = 0
    final_file = f"gpt_results_test_temp{temp}.txt"

    with open(final_file, 'w') as writer:

        for record in tqdm(data):
            text = record["context"]
            question = record["question"]
            choices = record["choices"]
            ans = None
            dists = []

            for choice in choices:
                if choice["type"]=="correct answer":
                    ans = choice["text"]
                else:
                    dists.append(choice["text"])

            if (current_file == "test.json") and (len(dists) < 3):
                continue

            while True:
                try:
                    final_prompt = f'{default_prompt}\n\nTexto: {text}\n\nPregunta: {question}\n\nRespuesta Correcta: {ans}'
                    # print(final_prompt)
                    gen_params = {
                        'prompt': final_prompt,
                        'temperature': temp,
                        'max_tokens': 1024
                    }
                    completion = openai.Completion.create(engine='text-davinci-003', **gen_params)
                    
                except openai.error.RateLimitError:
                    time.sleep(60)
                    continue

                generated_distractors = completion["choices"][0]['text']
                context_str = f"{CLS} {text} {SEP} {question} {SEP} {ans} {SEP}"
                writer.write(f"{context_str}{generated_distractors}\n{dists}\n\n")

                break
    
    