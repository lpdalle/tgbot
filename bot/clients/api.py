from bot.clients.generations import GenerationClient
from bot.clients.users import UserClient

base_url = 'http://127.0.0.1:5000'


class ApiClient:
    def __init__(self, url: str) -> None:
        self.generation = GenerationClient(url)
        self.users = UserClient(url)


api = ApiClient(base_url)
