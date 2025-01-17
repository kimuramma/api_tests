import os
from dotenv import load_dotenv

load_dotenv()

# uuid = os.getenv('UUID')
HOST = os.getenv('HOST')
class Endpoints:

    send_otp = f"{HOST}/ffc-api-public/universal/general/send-otp"
    validate_otp = f"{HOST}/ffc-api-public/universal/general/validate-otp"
    get_model2 = lambda self, iin: f"{HOST}ffc-api-public/universal/datalab/model2/{iin}"
    apply_lead = f"{HOST}/ffc-api-public/universal/apply/apply-lead"
    get_scoring_result = f"{HOST}/ffc-api-public/universal/general/scoring-result/"
    get_base_information = f"{HOST}/ffc-api-public/universal/general/base-information/"
    set_reference_id = f"{HOST}/ffc-api-public/universal/general/set-reference-id/"
    send_redirect_url = f"{HOST}/ffc-api-public/universal/general/send-redirect-url/"
    auth = f"{HOST}/ffc-api-auth/"
    frames_api = f"{HOST}/ru/frames-api/"

    def frames_urls_with_path(self, uuid, path):
        return f"{HOST}/ru/frames-api/{uuid}/{path}"
