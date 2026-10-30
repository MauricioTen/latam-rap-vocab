import os
import requests

class GeniusClient:
    def __init__(self, token: str | None = None):
        self.session = requests.Session()
        token = token or os.environ[____]
        self.session.headers["Authorization"] = f"____ {token}"