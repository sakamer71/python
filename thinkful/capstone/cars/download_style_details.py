__author__ = 'skamer'
import requests
import json
from time import sleep
from create_db_new import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import desc, asc

Session = sessionmaker(bind=engine)

## details by styleid https://api.edmunds.com/api/vehicle/v2/styles/200468025?view=full&fmt=json&api_key=b34wypjmb2fjf85asccqrv3z
## equipment by style id (dimensions + performance)  https://api.edmunds.com/api/vehicle/v2/styles/200468025/equipment?availability=standard&equipmentType=OTHER&fmt=json&api_key=b34wypjmb2fjf85asccqrv3z
def edmunds_get_style_details(style_id):
    #f = open('data/styles/{}_details.txt'.format(style_id), 'w+')
    with open('data/styles/{}_details.txt'.format(style_id), 'wb') as handle:
        url = 'https://api.edmunds.com/api/vehicle/v2/styles/{}?view=full&fmt=json&api_key=b34wypjmb2fjf85asccqrv3z'.format(style_id)
        r = requests.get(url, stream=True)
        if not r.ok:
            # Something went wrong
            pass
        for block in r.iter_content(1024):
            if not block:
                break
            handle.write(block)
    sleep(1)

def edmunds_get_style_equipment(style_id):
    #f = open('data/styles/{}_equipment.txt'.format(style_id), 'w+')
    with open('data/styles/{}_equipment.txt'.format(style_id), 'wb') as handle:
        url = 'https://api.edmunds.com/api/vehicle/v2/styles/{}/equipment?availability=standard&equipmentType=OTHER&fmt=json&api_key=b34wypjmb2fjf85asccqrv3z'.format(style_id)
        r = requests.get(url, stream=True)
        if not r.ok:
            # Something went wrong
            pass
        for block in r.iter_content(1024):
            if not block:
                break
            handle.write(block)
    sleep(1)

session = Session()
print "Querying the db now.................."
for i in session.query(Styles).order_by(asc(Styles.style_id)):
    mystyleid = i.style_id
    print mystyleid
    edmunds_get_style_details(mystyleid)
    edmunds_get_style_equipment(mystyleid)



