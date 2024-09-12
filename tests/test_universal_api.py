import os

from config.base_test import BaseTest


class TestUniversalAPI(BaseTest):
    uuid = None
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
        self.universal_frames.get_frames_api(self.uuid)
