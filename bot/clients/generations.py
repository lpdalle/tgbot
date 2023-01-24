import httpx

from bot.clients.schema import Generation


class GenerationClient:
    def __init__(self, url) -> None:
        self.url = url

    def get_for_user(self, user_id: int):
        url = f'{self.url}/api/v1/users/{user_id}/generations/'
        response = httpx.get(url)
        response.raise_for_status()
        if response.status_code == 404:  # noqa: WPS432
            return None
        return [Generation(**generation) for generation in response.json()]

    def add(self, user_id: int, prompt: str, status: str):
        url = f'{self.url}/api/v1/users/{user_id}/generations/'
        generation = {
            'user_id': user_id,
            'prompt': prompt,
            'status': status,
        }
        headers = {'Content-Type': 'application/json'}
        response = httpx.post(url, json=generation, headers=headers)
        return Generation(**response.json())

    def get_image(self, generation_id: int):
        url = f'{self.url}/api/v1/generations/{generation_id}/image'
        response = httpx.get(url)
        return response.content

    def check_status(self, generation_id: int):
        url = f'{self.url}/api/v1/generations/{generation_id}/complete'
        response = httpx.get(url)
        return Generation(**response.json())
