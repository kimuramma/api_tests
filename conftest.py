import os
from dotenv import load_dotenv, set_key
import requests
import pytest

ENV_PATH = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=ENV_PATH)
print(ENV_PATH, "\n\n\n\n\n")


HOST = os.getenv('HOST')



@pytest.fixture(autouse=True, scope="session")
def get_token():
    response = requests.post(
        url=f"{HOST}/ffc-api-auth/",
        data={

            "password": f"{os.getenv('PASSWORD')}",
            "username": f"{os.getenv('USERNAMEP')}"

        }
    )

    assert response.status_code == 200

    token = response.json().get('access')
    if token:
        # Записываем токен в файл .env
        set_key(ENV_PATH, "TOKEN", token)
        print(f"TOKEN записан в .env: {token}")
    else:
        print("Токен не был получен.")

    print(response.status_code, response.json())


@pytest.fixture(autouse=True, scope="session")
def get_user_token():
    response = requests.post(
        url=f"{HOST}/ffc-api-auth/",
        data={

            "password": f"{os.getenv('USER_PASSWORD')}",
            "username": f"{os.getenv('USERNAME2')}"

        }
    )
    print(ENV_PATH, "\n\n\n\n\n")
    print(os.getenv('USER_PASSWORD'),os.getenv('USERNAME2'))
    assert response.status_code == 200

    token = response.json().get('access')
    if token:
        # Записываем токен в файл .env
        set_key(ENV_PATH, "TOKEN2", token)
        print(f"TOKEN2 записан в .env: {token}")
    else:
        print("Токен2 не был получен.")

    print(response.status_code, response.json())