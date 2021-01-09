import requests
from requests.sessions import HTTPAdapter
from ipleak.app import console


def get_url(url: str, max_retries: int = 3) -> dict:
    session = requests.Session()
    session.mount('https://', HTTPAdapter(max_retries=max_retries))

    try:
        request = session.get(url)
        return request.json()
    except ConnectionError as e:
        return {}
