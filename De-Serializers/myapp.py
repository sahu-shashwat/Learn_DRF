import requests
import json

URL = "http://127.0.0.1:8000/studata/"

data = {"name": "malaya", "roll": 101, "city": "junagarh"}

json_data = json.dumps(data)
r = requests.post(url=URL, data=json_data)
print(r.text)
data = r.json()
print(data)
