import os

from config.base_test import BaseTest


class TestUniversalAPI(BaseTest):

    def test_universal_api(self):
        self.universal_api.send_otp()
        self.universal_api.validate_otp()
        #self.universal_api.get_model2()
        self.universal_api.apply_lead()
        self.universal_api.get_scoring_result()
