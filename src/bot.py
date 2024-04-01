
import requests
import os


def send_msg(text: str):
    token = os.environ['GOMU_BOT_TOKEN']
    chanel_id = os.environ['GOMU_CHANEL_ID']

    baseurl = "api.telegram.org"
    url = f"{baseurl}/bot{token}"
    payload = dict(user_id=chanel_id, text=text)

    try:
        requests.post(url=url, params=payload)
        raise Exception()
    except Exception as exc:
        print(type(exc))
