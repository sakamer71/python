__author__ = 'skamer'
from create_db_new import *
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

f=open('makes.txt','r')
f = f.read()
dict = eval(f)

print dict
for key in dict:
    print key

for x in dict['makes']:
    ##### Create Instances
    new = Make(make_id = x['id'], make = x['niceName'], make_n = x['name'])  ## create new row to add to db
    session = Session()
    ##### Write to make table of cars db
    session.add(new)
    session.commit()