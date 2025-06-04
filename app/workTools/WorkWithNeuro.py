import requests
import json

class WorkWithNeuro:
    @staticmethod
    def answer(promt, token):
        response = requests.post(
        url = "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization" : f"Bearer {token}",
            "Content-Type" : "application/json",
        },
        data=json.dumps({
            "model" : "deepseek/deepseek-r1-0528:free",
            "messages" : [
            {
                "role" : "user",
                "content" : f"{promt}. Отвечай на русском языке"
            }
            ],
            
        })
        )
        answer = response.json()['choices'][0]['message']['content']
        return answer