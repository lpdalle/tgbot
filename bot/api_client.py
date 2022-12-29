import requests

base_url = 'http://127.0.0.1:5000'


class GenerationClient:
    def __init__(self, url: str) -> None:
        self.url = url

    def add(self, user_id: int, prompt: str, status: str):
        url = f'{self.url}/api/v1/users/{user_id}/generation/'
        generation = {
            'prompt': prompt,
            'status': status,
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.request('POST', url, json=generation, headers=headers)
        response.raise_for_status()


class ApiClient:
    def __init__(self, url: str) -> None:
        self.generation = GenerationClient(url)


api = ApiClient(base_url)
