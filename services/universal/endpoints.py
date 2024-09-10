import os
from dotenv import load_dotenv

load_dotenv()

uuid = os.getenv('UUID')
HOST = "https://fastcash-back.trafficwave.kz"
class Endpoints:

    send_otp = f"{HOST}/ffc-api-public/universal/general/send-otp"
    validate_otp = f"{HOST}/ffc-api-public/universal/general/validate-otp"
    get_model2 = lambda self, iin: f"{HOST}ffc-api-public/universal/datalab/model2/{iin}"
    apply_lead = f"{HOST}/ffc-api-public/universal/apply/apply-lead"
    get_scoring_result = f"{HOST}/ffc-api-public/universal/general/scoring-result/{uuid}"