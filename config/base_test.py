from services.universal.api_universal import UniversalAPI

class BaseTest:
    def setup_method(self):
        self.universal_api = UniversalAPI()