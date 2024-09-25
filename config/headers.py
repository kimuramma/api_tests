import os
from dotenv import load_dotenv

load_dotenv()


class Headers:

    basic = {
        "Authorization": f"JWT {os.getenv('TOKEN')}"
    }
    wrong_jwt = {
        "Authorization": f"JWT {os.getenv('')}"
    }