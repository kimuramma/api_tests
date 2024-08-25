import os
HOST = "https://fastcash-back.trafficwave.kz"
class Endpoints:

    send_otp = f"{HOST}/ffc-api-public/universal/general/send-otp"
    validate_otp = f"{HOST}/ffc-api-public/universal/general/validate-otp"
    get_model2 = lambda self, iin: f"{HOST}ffc-api-public/universal/datalab/model2/{iin}"