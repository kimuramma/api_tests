class Payloads:
    send_otp = {
        "iin": "820507402189",
        "mobile_phone": "+77066078118"
    }
    validate_otp = {
        "iin": "820507402189",
        "mobile_phone": "+77066078118",
        "code": "0000"
    }
    apply_lead = {
    "iin": "820507402189",
    "mobile_phone": "+77066078118",
    "product": "VILED_CREDIT",
    "partner": "VILED",
    "channel": "VILED_WEB",
    "credit_params": {
        "period": 6,
        "principal": 10000
    },
    "additional_information": {
        "hook_url": "https://api-test.viled.kz/finance-gateway/api/ffin/result/success",
        "success_url": "",
        "failure_url": "",
        "reference_id": "",
        "delivery_address": ""
    }
}

    set_reference_id = {
  "reference_id": "TIGER01",
  "credit_params": {
    "period": 6,
    "principal": 10000
  },
  "product": "VILED_CREDIT"
}
    send_redirect_url = {
  "success": True
}
    auth_for_frames = {
        "username": "m.zhakeshov@globerce.capital",
        "password": ",z`1m%Sngci$%E))))"
    }