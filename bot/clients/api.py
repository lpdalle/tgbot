from bot.clients.generations import GenerationClient
from bot.clients.users import UserClient
from bot.config import conf


class ApiClient:
    def __init__(self, url: str) -> None:
        self.generation = GenerationClient(url)
        self.users = UserClient(url)


api = ApiClient(conf.base_url)
