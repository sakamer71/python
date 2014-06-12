__author__ = 'skamer'
import requests
import json
import pprint
from time import sleep

from create_db_new import *
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)


def edmunds_get_model(make):
    f = open('data/makes/{}_models.txt'.format(make), 'w+')
    url = 'https://api.edmunds.com/api/vehicle/v2/{}/models?state=new&year=2014&view=basic&fmt=json&api_key=b34wypjmb2fjf85asccqrv3z'.format(make)
    r = requests.get(url)
    t = r.text
    #print t
    #j = r.json()
    #print j
    f.write(t)
    f.close()
    sleep(1)  ## b/c the edmunds api has a limit of how many queries per second.. and we dont want bad data

#edmunds_get_models('bmw')

'''
f = open('bmw.txt','r')
dict = eval(f.read())
print type(dict)
for key in dict:
    if key =='modelsCount':
        myrange = int(dict[key])
        print "the modelscount is {}".format(myrange)

for i in range(myrange):
    print dict['models'][i]['id'], dict['models'][i]['name'], dict['models'][i]['niceName'], dict['models'][i]['years'][0]['id']

### pretty print
pp = pprint.PrettyPrinter(indent=2)
#pp = pprint.pprint(dict)
'''

def get_all_models_from_edmunds():
    session = Session()
    print "Querying the db now.................."
    for i in session.query(Make):
        mymake = i.make
        print "writing {}_models.txt file".format(i.make)
        print i.make, i.make_id, i.make_n
        edmunds_get_model(mymake)

def update_models_db():
    session = Session()
    print "Querying the db now.................."
    for i in session.query(Make):
        mymake = i.make
        mymake_id = i.make_id
        print "querying {}_models.txt file".format(i.make)
        f = open('data/makes/{}_models.txt'.format(mymake), 'r')
        dict = eval(f.read())
        for key in dict:
            if key =='modelsCount':
                myrange = int(dict[key])
                print "the modelscount is {}".format(myrange)

        for i in range(myrange):  ## the range of models from the json in {make}_models.txt
            print dict['models'][i]['id'], dict['models'][i]['name'], dict['models'][i]['niceName'], dict['models'][i]['years'][0]['id']
            mymodelname = dict['models'][i]['name']
            mymodelname_n = dict['models'][i]['niceName']
            mymodelid = dict['models'][i]['years'][0]['id']
            myyear = 2014

            ##### Create Instances
            ##model_id, model, model_n, year, make_id
            new = Model(model_id = mymodelid, model = mymodelname, model_n = mymodelname_n, year = myyear, make_id = mymake_id )  ## create new row to add to db
            session = Session()
            ##### Write to make table of cars db
            session.add(new)
            session.commit()
        print '-----------------\n'
#get_all_models_from_edmunds()
update_models_db()
