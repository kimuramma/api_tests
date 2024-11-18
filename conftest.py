import os
from dotenv import load_dotenv, set_key
import requests
import pytest



ENV_PATH = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(ENV_PATH)

HOST = "https://fastcash-back.trafficwave.kz"



@pytest.fixture(autouse=True, scope="session")
def get_token():
    response = requests.post(
        url=f"{HOST}/ffc-api-auth/",
        data={

            "password": f"{os.getenv('PASSWORD')}",
            "username": f"{os.getenv('USERNAME_FASTCASH')}"

        }
    )

    assert response.status_code == 200

    token = response.json().get('access')
    if token:
        # Записываем токен в файл .env
        set_key( ENV_PATH ,"TOKEN", token)
        print(f"TOKEN записан в .env: {token}")
    else:
        print("Токен не был получен.")

    print(response.status_code, response.json())
