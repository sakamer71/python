
__author__ = 'skamer'
false = False
from create_db_new import *
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
from pprint import PrettyPrinter
print "Querying the db"

'''
## Example on how to update an existing row
## first find the row
## then update the columns
## then add and commit to the session

test = session.query(Test).filter_by(name='bill').first()
test.color = 'reddish'
session.add(test)
session.commit()
'''

'''
#f = open('data/styles/101286108_equipment.txt','r')
f = open('data/styles/200493786_details.txt','r')
d = eval(f.read())

print d
pp = PrettyPrinter(indent=4)
pp.pprint(d)
eng_cylinder = d['engine']['cylinder']
print eng_cylinder
fueltype_id = d['engine']['type']
print fueltype_id
eng_torque = d['engine']['torque']
print eng_torque
eng_displacement = d['engine']['displacement']
print eng_displacement
eng_hp = d['engine']['horsepower']
print eng_hp
doors = d['numOfDoors']
print doors
transmission = d['transmission']['transmissionType']
print transmission
price_msrp = d['price']['baseMSRP']
print price_msrp
price_invoice = d['price']['baseInvoice']
print price_invoice
drivenwheels = d['drivenWheels']
print drivenwheels
body_size = d['categories']['vehicleSize']
bodytype = d['categories']['vehicleStyle']
mpg_hwy = d['MPG']['highway']
mpg_city = d['MPG']['city']
print body_size
print bodytype
print mpg_hwy
print mpg_city


## get more details from the equipment file
f = open('data/styles/101286108_equipment.txt','r')
d = eval(f.read())

print d
pp = PrettyPrinter(indent=4)
#pp.pprint(d)
### get list of style-ids from database
mycount = int(d['equipmentCount'])
'''

for i in session.query(Styles):
    print '---------------------------------------------------------------'
    mystyleid = int(i.style_id)
    ## get data from the details file
    s = session.query(Styles).filter_by(style_id=mystyleid).first()
    #test.color = 'reddish'
    #session.add(test)
    #session.commit()
    print "Details for styleid {}".format(mystyleid),
    f = open('data/styles/{}_details.txt'.format(mystyleid),'r')
    d = eval(f.read())
    f.close()
    #print d
    #pp = PrettyPrinter(indent=4)
    #pp.pprint(d)
    try: s.eng_cylinder = d['engine']['cylinder']
    except: s.eng_cylinder = None
    print s.eng_cylinder,
    try: s.fueltype = d['engine']['type']
    except: s.fueltype = None
    print s.fueltype,
    try: s.eng_torque = d['engine']['torque']
    except: s.eng_torque = None
    print s.eng_torque,

    try: s.eng_displacement = d['engine']['displacement']
    except: s.eng_displacement = None
    print s.eng_displacement,
    try: s.eng_hp = d['engine']['horsepower']
    except: s.eng_hp = None
    print s.eng_hp,
    try: s.doors = d['numOfDoors']
    except: s.doors = None
    print s.doors,
    try: s.transmission = d['transmission']['transmissionType']
    except: s.transmission = None
    print s.transmission,
    try: s.price_msrp = d['price']['baseMSRP']
    except: s.price_msrp
    print s.price_msrp,
    try: s.price_invoice = d['price']['baseInvoice']
    except: s.price_invoice = None
    print s.price_invoice,
    try: s.drivenwheels = d['drivenWheels']
    except: s.drivenwheels = None
    print s.drivenwheels,
    try: s.body_size = d['categories']['vehicleSize']
    except: s.body_size = None
    try: s.bodytype = d['categories']['vehicleStyle']
    except: s.bodytype = None
    try: s.mpg_hwy = d['MPG']['highway']
    except: s.mpg_hwy = None
    try: s.mpg_city = d['MPG']['city']
    except: s.mpg_city = None
    print s.body_size,
    print s.bodytype,
    print s.mpg_hwy,
    print s.mpg_city,


    f = open('data/styles/{}_equipment.txt'.format(mystyleid),'r')
    d = eval(f.read())
    f.close()
    print "Equipment for styleid {}".format(mystyleid),
    mycount = int(d['equipmentCount'])
    for i in range(mycount):
        #print "attribute {}: ".format(i),
        #print d['equipment'][i]['attributes']
        for i in d['equipment'][i]['attributes']:
            if i['name'] == '1st Row Head Room':
                s.headroom_1st = i['value']
            if i['name'] == '2nd Row Head Room':
                s.headroom_2nd = i['value']
            if i['name'] == '1st Row Leg Room':
                s.legroom_1st = i['value']
            if i['name'] == '2nd Row Leg Room':
                s.legroom_2nd = i['value']
            if i['name'] == 'Cargo Capacity, All Seats In Place':
                s.cargo_capacity == i['value']
            if i['name'] == 'Manufacturer 0 60mph Acceleration Time (seconds)':
                s.zero_to_sixty == i['value']
                #else:
                #   print i['name']
    ### parse text files for the data we want
    print "zerotosixty: {} cargo: {} 1st head: {} 2nd head: {} 1st leg: {} 2nd leg: {}".format(s.zero_to_sixty, s.cargo_capacity,s.headroom_1st,s.headroom_2nd,s.legroom_1st,s.legroom_2nd)
    # session.add(s)
    #session.commit()
## update database


