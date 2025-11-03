import requests 
import json

URL = "http://127.0.0.1:8000/studata/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.get(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)

# get_data(2)


def post_data():
    data = {
        'name':'Rp Rahman',
        'roll':102,
        'city':'minecraft'
    }
    headers = {'Content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)

# post_data()

def update():
    data = {
        'id':2,
        'name':'Shoheb'
    }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)

# update()

def delete_data():
    data = {'id':4}
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.delete(url=URL, headers=headers, data=json_data)
    data = r.json()
    print(data)

delete_data()