import requests

def check_connection():
    """Försöker koppla upp till HKRs hemsida under 5 sekunder,
        returnerar True om det går och false om det har passerat 5 sekunder
        utan lycka."""
    URL = "https://www.hkr.se/"
    TIMEOUT = 5 

    print("Checking internet connection...")

    try:
        requests.get(URL, timeout=TIMEOUT)
        print("Internet is accessible...")
        return True
    except (requests.ConnectionError, requests.Timeout):
        print("Internet is not accessible...")
        return False