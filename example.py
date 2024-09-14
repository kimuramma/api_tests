import requests

HOST = "https://fastcash-back.trafficwave.kz"

response = requests.post(
    url=f"{HOST}/ffc-api-auth/",
    data={
    "password": ",z`1m%Sngci$%E))))",
    "username": "m.zhakeshov@globerce.capital"
}
)

print(response.status_code, response.json())