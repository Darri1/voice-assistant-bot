import requests

from creds import get_creds

IAM_TOKEN, FOLDER_ID = get_creds()


def text_to_speech(text):
    headers = {
        "Authorization": f"Bearer {IAM_TOKEN}",
    }
    data = {
        "text": text,
        "lang": "ru-RU",
        "voice": "filipp",
        "folderId": FOLDER_ID,
    }

    response = requests.post(
        "https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize",
        headers=headers,
        data=data,
    )

    if response.status_code == 200:
        return True, response.content
    else:
        return False, "При запросе в SpeechKit произошла ошибка"


def speech_to_text(data):
    params = "&".join(["topic=general", f"folderId={FOLDER_ID}", "lang=ru-RU"])

    headers = {
        "Authorization": f"Bearer {IAM_TOKEN}",
    }

    response = requests.post(
        f"https://stt.api.cloud.yandex.net/speech/v1/stt:recognize?{params}",
        headers=headers,
        data=data,
    )

    decoded_data = response.json()

    if decoded_data.get("error_code") is None:
        return True, decoded_data.get("result")
    else:
        return False, "При запросе в SpeechKit произошла ошибка"
