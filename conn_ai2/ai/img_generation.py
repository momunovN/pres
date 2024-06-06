
import requests
import base64
import time
from random import randint


def generate_image(prompt_text):
    prompt = {
        "modelUri": "art://b1gvhp2b702b3kvoqti3/yandex-art/latest",
        "generationOptions": {
            "seed": randint(10000, 2000000)
        },
        "messages": [
            {
                "weight": 1,
                "text": prompt_text
            }
        ]
    }


    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/imageGenerationAsync"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key AQVNwJ0beANsfkeszeGmC7BPmiqLB9uPpJuYGFtj"
    }
    print()
    response = requests.post(url=url, headers=headers, json=prompt)
    result = response.json()

    operation_id = result['id']
    operation_url = f"https://llm.api.cloud.yandex.net:443/operations/{operation_id}"
    while True:
        operation_response = requests.get(url=operation_url, headers=headers)
        operation_result = operation_response.json()
        if 'response' in operation_result:
            image_base64 = operation_result['response']['image']
            image_data = base64.b64decode(image_base64)
            return image_data
        else:
            print('Ожидайте, изображение не готово')
            time.sleep(5)
