from time import sleep
from urllib.parse import urljoin
from uuid import UUID

import requests
from dotenv import set_key

from conftest import ENV_PATH
from example import response
from services.universal.endpoints import Endpoints
from services.universal.payloads import Payloads
from config.headers import Headers


class UniversalFrames:
    def __init__(self):
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    def auth_for_frames(self):
        response = requests.post(
            url=self.endpoints.auth,
            json=self.payloads.auth_for_frames
        )
        print(response.status_code, response.json())
        print('Токен получен')
        assert response.status_code == 200, response.json()