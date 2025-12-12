import requests

BASE_URL = "https://backend-557891328232.us-central1.run.app"

def add(x, y):
    payload = {"x": x, "y": y}
    r = requests.post(f"{BASE_URL}/add", json=payload)
    r.raise_for_status()
    return r.json()["result"]

def ask_llm(prompt):
    r = requests.post(f"{BASE_URL}/ask_llm", json={"prompt": prompt})
    r.raise_for_status()
    return r.json()["output"]

