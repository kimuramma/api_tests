import os
from dotenv import load_dotenv
import requests
import pytest

load_dotenv()

HOST = "https://fastcash-back.trafficwave.kz"

@pytest.fixture(autouse=True, scope="session")
def get_token():
    response = requests.post(
        url=f"{HOST}/ffc-api-auth/",
        data={

            "password": f"{os.getenv('PASSWORD')}",
            "username": f"{os.getenv('USERNAME')}"

        }
    )
    assert response.status_code == 200
    print(response.status_code, response.json())