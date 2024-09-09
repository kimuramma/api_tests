import os

from config.base_test import BaseTest


class TestUniversalAPI(BaseTest):

    def test_universal_api(self):
        self.universal_api.send_otp()
