from services.universal.api_universal import UniversalAPI
from services.universal.universal_frames import UniversalFrames


class BaseTest:
    def setup_method(self):
        self.universal_api = UniversalAPI()
        self.universal_frames = UniversalFrames()
