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
        assert response.status_code == 200, f"Expected status 200, but got {response.status_code}"
        response.json()

        model = AuthModel(**response.json())
        return model

    def get_frames_fraud(self, uuid: UUID):
        fraud_path = "fraud"
        frames_fraud_url = self.endpoints.frames_urls_with_path(uuid, fraud_path)
        print(frames_fraud_url)
        response = requests.get(
            url=frames_fraud_url,
            headers=self.headers.basic2
        )
        print(response.status_code, response.json())
        print('Информация для фреймов получена')
        assert response.status_code == 200, f"Expected status 200, but got {response.status_code}"
        response.json()

    def post_frames_fraud(self, uuid: UUID):
        fraud_path = "fraud"
        frames_fraud_url = self.endpoints.frames_urls_with_path(uuid, fraud_path)
        print(frames_fraud_url)
        response = requests.post(
            url=frames_fraud_url,
            headers=self.headers.basic2,
            json=self.payloads.post_fraud
        )
        print(response.status_code, response.json())
        print('Информация для фреймов получена')
        assert response.status_code == 200, f"Expected status 200, but got {response.status_code}"
        response.json()

    def get_biometry(self, uuid: UUID):
        biometry_path = "biometry"
        frames_biometry_url = self.endpoints.frames_urls_with_path(uuid, biometry_path)
        print(frames_biometry_url)
        response = requests.get(
            url=frames_biometry_url,
            headers=self.headers.basic2
        )
        print(response.status_code, response.json())
        print('Данные для биометрий получены')
        assert response.status_code == 200, f"Expected status 200, but got {response.status_code}"
        response.json()

    def post_biometry(self, uuid: UUID):
        biometry_path = "biometry"
        frames_biometry_url = self.endpoints.frames_urls_with_path(uuid, biometry_path)
        print(frames_biometry_url)
        response = requests.post(
            url=frames_biometry_url,
            headers=self.headers.basic2,
            json=self.payloads.mock_biometry
        )
        print(response.status_code, response.json())
        print('Данные для биометрий получены')
        assert response.status_code == 200, f"Expected status 200, but got {response.status_code}"
        response.json()

    def get_signature(self, uuid: UUID):
        signature_path = "signature"
        frames_signature_url = self.endpoints.frames_urls_with_path(uuid, signature_path)
        print(frames_signature_url)
        response = requests.get(
            url=frames_signature_url,
            headers=self.headers.basic2
        )
        print(response.status_code, response.json())
        print('Get signatur passed')
        assert response.status_code == 200, f"Expected status 200, but got {response.status_code}"
        response.json()

    def post_signature(self, uuid: UUID):
        signature_path = "signature"
        frames_signature_url = self.endpoints.frames_urls_with_path(uuid, signature_path)
        print(frames_signature_url)
        response = requests.post(
            url=frames_signature_url,
            headers=self.headers.basic2,
            json=self.payloads.signature
        )
        print(response.status_code, response.json())
        print('POST signature passed')
        assert response.status_code == 200, f"Expected status 200, but got {response.status_code}"
        response.json()