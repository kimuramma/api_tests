import os
from dotenv import load_dotenv

load_dotenv()


class Headers:

    basic = {
        "Authorization": f"JWT {os.getenv('TOKEN')}"
    }
    basic2 = {
        "Authorization": f"JWT {os.getenv('TOKEN2')}"
    }
    wrong_jwt = {
        "Authorization": f"JWT {os.getenv('')}"
    }