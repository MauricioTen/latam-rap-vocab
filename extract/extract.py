import os
import requests

class GeniusClient:
    def __init__(self, token: str | None = None):
        self.session = requests.Session()
        token = token or os.environ["GENIUS_ACCESS_TOKEN"]
        self.session.headers["Authorization"] = f"Bearer {token}"