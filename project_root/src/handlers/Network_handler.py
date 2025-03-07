import requests

def check_connection():
    URL = "https://www.hkr.se/"
    TIMEOUT = 5 

    try:
        requests.get(URL, timeout=TIMEOUT)
        print("Internet is accessible")
        return True
    except (requests.ConnectionError, requests.Timeout):
        print("Internet is not accessible")
        return False