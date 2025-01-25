import requests
from tinydb import TinyDB

db=TinyDB('randomuser.json',indent=4)

response=requests.get('https://randomuser.me/api/?results=5')
user=response.json()["results"]
for i in user:
    db.insert({"name":i["name"]["first"],"last_name":i["name"]["last"],"age":i["dob"]["age"],"gender":i["gender"]})  