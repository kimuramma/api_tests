import os

import allure
import pytest

from config.base_test import BaseTest

@allure.epic("Universal API Flow")
@allure.feature("Universal API")
class TestUniversalAPI(BaseTest):
    uuid = None
    @pytest.mark.regression
    @allure.title("Universal API end2end")
    def test_universal_api(self):
        self.universal_api.send_otp()
        self.universal_api.validate_otp()
        #self.universal_api.get_model2()
        self.uuid = self.universal_api.apply_lead()
        self.universal_api.get_scoring_result(self.uuid)
        self.universal_api.get_base_information(self.uuid)
        self.universal_api.set_reference_id(self.uuid)
        self.universal_api.send_redirect_url(self.uuid)
        self.universal_frames.auth_for_frames()
        self.universal_frames.get_frames_fraud(self.uuid)
        self.universal_frames.get_frames_fraud(self.uuid)
        self.universal_frames.post_frames_fraud(self.uuid)
        self.universal_frames.get_biometry(self.uuid)
        self.universal_frames.post_biometry(self.uuid)
        self.universal_frames.get_signature(self.uuid)
        self.universal_frames.post_signature(self.uuid)

#class TestUniversalAPiAuth(BaseTest):
#    def test_universal_api_auth(self):
#        self.universal_api.auth()
#        self.universal_api.auth_with_invalid_username()
#        self.universal_api.auth_with_invalid_password()