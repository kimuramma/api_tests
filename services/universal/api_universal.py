from time import sleep
from urllib.parse import urljoin
from uuid import UUID

import allure
import requests
from dotenv import set_key

from conftest import ENV_PATH
from example import response
from services.universal.endpoints import Endpoints
from services.universal.payloads import Payloads
from config.headers import Headers
from services.universal.models.universal_api_models import GetScoringResultModel
from utils.helper import Helper


class UniversalAPI(Helper):
    def __init__(self):
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()
    @allure.step("Send OTP")
    def send_otp(self):
        response = requests.post(
            url=self.endpoints.send_otp,
            headers=self.headers.basic,
            json=self.payloads.send_otp
        )
        print(response.json())
        print('Запрос ОТП прошла успешно')
        assert response.status_code == 200, f"Expected status 200, but got {response.status_code}"
        self.attach_response(response.json())

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

    def apply_lead(self) -> UUID:
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
        return uuid

    def get_scoring_result(self, uuid: UUID):
        get_scoring_result = urljoin(self.endpoints.get_scoring_result, str(uuid))
        for i in range(10):
            response = requests.get(
                url=get_scoring_result,
                headers=self.headers.basic
            )
            print(response.status_code, response.text)
            if response.status_code == 204:
                sleep(5)
            else:
                break
        print(response.status_code, response.json())
        print('Результаты скоринга получены')
        assert response.status_code == 200, response.json()
        model = GetScoringResultModel(**response.json())
        return model

    def get_base_information(self, uuid: UUID):
        get_base_information = urljoin(self.endpoints.get_base_information, str(uuid))
        response = requests.get(
            url=get_base_information,
            headers=self.headers.basic
        )
        print(response.status_code, response.json())
        print('Базовая информация получена')
        assert  response.status_code == 200, response.json()

    def set_reference_id(self, uuid: UUID):
        set_reference_id = urljoin(self.endpoints.set_reference_id, str(uuid))
        response = requests.put(
            url=set_reference_id,
            headers=self.headers.basic,
            json=self.payloads.set_reference_id
        )
        print(response.status_code, response.json())
        print('Продукт выбран')
        assert response.status_code == 200, response.json()

    def send_redirect_url(self, uuid: UUID):
        send_redirect_url = urljoin(self.endpoints.send_redirect_url, str(uuid))
        response = requests.post(
            url=send_redirect_url,
            headers=self.headers.basic,
            json=self.payloads.send_redirect_url
        )
        print(response.status_code, response.json())
        print('Запрос на отправку СМС со ссылкой отправлен')
        assert response.status_code == 200, response.json()

