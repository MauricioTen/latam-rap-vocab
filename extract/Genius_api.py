import os
import requests

BASE_URL = "https://api.genius.com"

class GeniusClient:
    def __init__(self, token: str | None = None):
        self.session = requests.Session()
        token = token or os.environ["GENIUS_ACCESS_TOKEN"]
        self.session.headers["Authorization"] = f"Bearer {token}"


    def _get(self, path: str, **params) -> dict:
        resp = self.session.get(f"{BASE_URL}{path}", params=params, timeout =30)
        resp.raise_for_status()           # raises an exception on 4xx/5xx
        return resp.json()["response"]

