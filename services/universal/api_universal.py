import requests
from dotenv import set_key

from conftest import ENV_PATH
from example import response
from services.universal.endpoints import Endpoints
from services.universal.payloads import Payloads
from config.headers import Headers


class UniversalAPI:
    def __init__(self):
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    def send_otp(self):
        response = requests.post(
            url=self.endpoints.send_otp,
            headers=self.headers.basic,
            json=self.payloads.send_otp
        )
        print(response.json())
        print('Запрос ОТП прошла успешно')
        assert response.status_code == 200, f"Expected status 200, but got {response.status_code}"

    def validate_otp(self):
        response = requests.post(
            url=self.endpoints.validate_otp,
            headers=self.headers.basic,
            json=self.payloads.validate_otp
        )
        print(response.json())
        print('Валидация ОТП прошла успешно')

        assert response.status_code == 200, response.json()

    def get_model2(self):
        response = requests.get(
            url=self.endpoints.get_model2,
            headers=self.headers.basic
        )
        print(response.json())
        assert response.status_code == 200, response.json()

    def apply_lead(self):
        response = requests.post(
            url=self.endpoints.apply_lead,
            headers=self.headers.basic,
            json=self.payloads.apply_lead
        )
        print(response.json())
        print('Заявка создалась успешно')
        assert response.status_code == 202, response.json()

        uuid = response.json().get('uuid')
        if uuid:
            # Записываем токен в файл .env
            set_key(ENV_PATH, "UUID", uuid)
            print(f"UUID записан в .env: {uuid}")
        else:
            print("UUID не был получен.")

        print(response.status_code, response.json())

    def get_scoring_result(self):
        response = requests.get(
            url=self.endpoints.get_scoring_result,
            headers=self.headers.basic
        )
        print(response.status_code, response.json())
        print('Результаты скоринга получены')
        assert response.status_code == 200, response.json()