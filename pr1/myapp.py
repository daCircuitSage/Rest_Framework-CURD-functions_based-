import requests
import json


URL = "http://127.0.0.1:8000/studata/"

def get_data(id = None):
    data = {}
    if data is not None:
        data = {'id':id}
        json_data = json.dumps(data)
        r = requests.get(url=URL, data=json_data)
        data = r.json()
        print(data)

# get_data(2)

def create_data():
    data = {
        'name':'NoONe',
        'roll':201,
        'city':'NoCity'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)

create_data()

def update_data():
    data = {
        'id':2,
        'name':'BandLoard'
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)

# update_data()