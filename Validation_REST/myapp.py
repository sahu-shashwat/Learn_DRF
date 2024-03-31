import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"


def get_data(id=None):
    data = {}
    if id is not None:
        data = {"id": id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)


# get_data(4) #it give only one vlaue
# get_data() #this will give all the values


def post_data():
    data = {"name": "Ramesh", "roll": 107, "city": "Hydrabad"}
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)

post_data()

def update_data():
    data = {"id": 6, "name": "Rupa",'roll':106, "city": "Bararh"}
    json_data = json.dumps(data)
    r = requests.put(url=URL,data=json_data)
    data=r.json()
    print(data)
# update_data()

def delete_data(id):
    data={'id':id}
    json_data = json.dumps(data)
    r = requests.delete(url=URL,data=json_data)
    data=r.json()
    print(data)
# delete_data(5)