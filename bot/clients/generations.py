import httpx


class GenerationClient:
    def __init__(self, url) -> None:
        self.url = url

    def get_for_user(self, user_id: int):
        url = f'{self.url}/api/v1/users/{user_id}'
        response = httpx.get(url)
        response.raise_for_status()
        if response.status_code == 404:  # noqa: WPS432
            return None
        return response.json()

    def add(self, user_id: int, prompt: str, status: str):
        url = f'{self.url}/api/v1/users/{user_id}/generation/'
        generation = {
            'user_id': user_id,
            'prompt': prompt,
            'status': status,
        }
        headers = {'Content-Type': 'application/json'}
        response = httpx.post(url, json=generation, headers=headers)
        response.raise_for_status()
