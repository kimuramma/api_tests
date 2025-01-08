import os
class Payloads:
    send_otp = {
        "iin": f"{os.getenv('IIN')}"
        ,
        "mobile_phone": f"{os.getenv('MOBILE_PHONE')}"
    }
    validate_otp = {
        "iin": f"{os.getenv('IIN')}",
        "mobile_phone": f"{os.getenv('MOBILE_PHONE')}",
        "code": f"{os.getenv('OTP_CODE')}"
    }
    apply_lead = {
        "iin": f"{os.getenv('IIN')}",
        "mobile_phone": f"{os.getenv('MOBILE_PHONE')}",
        "product": f"{os.getenv('PRODUCT')}",
        "partner": f"{os.getenv('PARTNER')}",
        "channel": f"{os.getenv('CHANNEL')}",
        "credit_params": {
            "period": 6,
            "principal": 10000
        },
        "additional_information": {
            "hook_url": "",
            "success_url": "",
            "failure_url": "",
            "reference_id": "",
            "delivery_address": ""
        }
    }

    set_reference_id = {
        "reference_id": "AUTOTEST",
        "credit_params": {
            "period": 6,
            "principal": 10000
        },
        "product": f"{os.getenv('PRODUCT')}"
    }
    send_redirect_url = {
        "success": True
    }
    auth_for_frames = {
        "username": f"{os.getenv('USERNAME2')}",
        "password": f"{os.getenv('USER_PASSWORD')}"
    }

    auth_invalid_username = {
        "username": f"{os.getenv('INVALID_USERNAME')}",
        "password": f"{os.getenv('USER_PASSWORD')}"
    }
    auth_invalid_password = {
        "username": f"{os.getenv('USERNAME2')}",
        "password": f"{os.getenv('INVALID_PASSWORD')}"
    }

    fraud_payload = {
        "fraud": "true",
        "approval_extra_move": "0",
        "agreement_extra_move": "true",
        "extra_move_type": "NO_EXTRA_MOVE"
    }
    mock_biometry = {

        "mock_biometry": True

    }

    post_fraud = {
        "fraud": "true",
        "approval_extra_move": "0",
        "agreement_extra_move": "true",
        "extra_move_type": "NO_EXTRA_MOVE"
    }

    signature = {
        "sms": "0000"
    }
