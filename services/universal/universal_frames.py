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
from services.universal.models.universal_api_models import AuthModel


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

        model = AuthModel(**response.json())
        return model

    def get_frames_api(self, uuid: UUID):
        frames_api_url = urljoin(self.endpoints.frames_api, str(uuid))
        print(frames_api_url)
        response = requests.get(
            url=frames_api_url,
            headers=self.headers.basic
        )
        print(response.status_code, response.json())
        print('Информация для фреймов получена')
