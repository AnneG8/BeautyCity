import requests
from django.conf import settings


def send_code(phone: str, vcode: int):
    url = 'https://smsc.ru/sys/send.php'
    message = f'BeautyCity: ваш код аутентификации: {vcode}'

    params = {
        'login': settings.SMSC_LOGIN,
        'psw': settings.SMSC_PSW,
        'phones': phone,
        'mes': message,
        'fmt': 3,
        'cost': 3
    }

    try:
        response = requests.post(url, data=params)
        response.raise_for_status()
        result = response.json()
        if 'error' in result:
            return False
        return True
    except requests.exceptions.HTTPError:
        return False
