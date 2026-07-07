import requests
import os

SENDER_EMAIL = "bluestock.analytics@gmail.com"

API_KEY = os.getenv("BREVO_API_KEY")
print("BREVO_API_KEY =", API_KEY)


def send_email_otp(receiver_email, otp):

    url = "https://api.brevo.com/v3/smtp/email"

    headers = {
        "accept": "application/json",
        "api-key": API_KEY,
        "content-type": "application/json"
    }

    payload = {
        "sender": {
            "name": "Bluestock Mutual Fund Analytics",
            "email": SENDER_EMAIL
        },
        "to": [
            {
                "email": receiver_email
            }
        ],
        "subject": "Password Reset OTP",
        "textContent": f"""
Hello,

Your OTP is:

{otp}

This OTP is valid for 5 minutes.

Regards,
Bluestock Mutual Fund Analytics
"""
    }

    try:

        response = requests.post(
            url,
            headers=headers,
            json=payload
        )

        print(response.status_code)
        print(response.text)

        return response.status_code == 201

    except Exception as e:
        print(e)
        return False
