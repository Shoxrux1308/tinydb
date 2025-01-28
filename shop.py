from tinydb import TinyDB

db=TinyDB('shop_db.json',indent=4)
db.insert({'name':'Macbook Pro','price':1800,'color':'Space Grey','memory':256})
db.insert({'name':'iPhone 15 Pro','price':1400,'color':'Black','memory':512})
db.insert({'name':'Samsung Galaxy S24 Ultra','price':1200,'color':'Black','memory':128})