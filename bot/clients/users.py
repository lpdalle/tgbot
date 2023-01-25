import httpx

from bot.clients.schema import User


class UserClient:
    def __init__(self, url: str) -> None:
        self.url = url

    def get_by_id(self, user_id: int):
        url = f'{self.url}/api/v1/users/{user_id}'
        response = httpx.get(url)
        if response.status_code == 404:  # noqa: WPS432
            return None
        response.raise_for_status()
        return User(**response.json())

    def get_by_tg_id(self, telegram_id: str):
        url = f'{self.url}/api/v1/users/telegram/{telegram_id}'
        response = httpx.get(url)
        if response.status_code == 404:  # noqa: WPS432
            return None
        response.raise_for_status()
        return User(**response.json())

    def add(self, login: str, email: str, telegram_id=None):
        url = f'{self.url}/api/v1/users/'
        user = {
            'login': login,
            'email': email,
            'telegram_id': telegram_id,
        }
        headers = {'Content-Type': 'application/json'}
        response = httpx.post(url, json=user, headers=headers, timeout=10)
        response.raise_for_status()
