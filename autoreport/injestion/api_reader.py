import requests
import pandas as pd


def read_api(url):

    response = requests.get(url, timeout=30)

    response.raise_for_status()

    data = response.json()

    return pd.json_normalize(data)