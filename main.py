from tinydb import TinyDB

db = TinyDB('db.json', indent=4)

db.insert({'name': 'Abdumajid',"lastname":"Abdulazizov", "job":"Student"})
db.insert({'name': 'Mehroj',"lastname":"abdullayev" ,"job":"Developer"})
