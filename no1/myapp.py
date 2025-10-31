import requests
import json

URL = "http://127.0.0.1:8000/studata/"

def get_data(id=None):
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
        'name':'Ghostdev',
        'roll':'125',
        'city':'GhostCity'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)

# create_data()

def modify():
    data = {
        'id': 3,
        'name':'JamesBondFortest',
        'city':'LosCity'
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)

modify()