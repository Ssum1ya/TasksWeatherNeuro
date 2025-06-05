import requests
import json
import aiohttp

class WorkWithNeuro:
    @staticmethod
    #async def answer(promt, token):
        # async with requests.post(
        # url = "https://openrouter.ai/api/v1/chat/completions",
        # headers={
        #     "Authorization" : f"Bearer {token}",
        #     "Content-Type" : "application/json",
        # },
        # data=json.dumps({
        #     "model" : "deepseek/deepseek-r1-0528:free",
        #     "messages" : [
        #     {
        #         "role" : "user",
        #         "content" : f"{promt}. Отвечай на русском языке"
        #     }
        #     ],
            
        # })
        # ) as response:
        #     answer = await response.json()
        #     data = answer['choices'][0]['message']['content']
        #     return data

    async def generate_response(prompt, token):
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers={
            "Authorization" : f"Bearer {token}",
            "Content-Type" : "application/json",
        }
        data=json.dumps({
            "model" : "deepseek/deepseek-r1-0528:free",
            "messages" : [
            {
                "role" : "user",
                "content" : f"{prompt}. Отвечай на русском языке"
            }
            ],
            
        })
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers = headers, data = data) as response:
                answer = await response.json()
                return answer['choices'][0]['message']['content']