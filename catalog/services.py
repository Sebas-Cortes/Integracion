import requests

def get_med():
    url = 'http://127.0.0.1:8000/api/Lote/'
    r = requests.get(url)
    med = r.json()
    return med