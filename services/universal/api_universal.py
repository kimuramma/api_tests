import requests

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
            url = self.endpoints.send_otp,
            headers = self.headers.basic,
            json = self.payloads.send_otp
        )
        print(response.json())
        assert response.status_code == 200,response.json()

