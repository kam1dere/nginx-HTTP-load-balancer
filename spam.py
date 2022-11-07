import requests
import time

time.sleep(20)
for i in range(270):
    r = requests.get("http://127.0.0.1:8989")
    time.sleep(1)
