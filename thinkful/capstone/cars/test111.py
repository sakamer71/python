__author__ = 'skamer'
from pprint import PrettyPrinter
false = False
mystyleid = 200695327
f = open('data/styles/200695327_equipment.txt','r')
d = eval(f.read())
#print d
pp = PrettyPrinter(indent=4)
#pp.pprint(d)
f = open('data/styles/{}_equipment.txt'.format(mystyleid),'r')
d = eval(f.read())
f.close()
print "Equipment for styleid {}".format(mystyleid),
mycount = int(d['equipmentCount'])
for i in range(mycount):
    #print "attribute {}: ".format(i),
    #print d['equipment'][i]['attributes']
    for i in d['equipment'][i]['attributes']:
        print i['name'], i['value']
        if i['name'] == '1st Row Head Room':
            headroom_1st = i['value']
        if i['name'] == '2nd Row Head Room':
            headroom_2nd = i['value']
        if i['name'] == '1st Row Leg Room':
            legroom_1st = i['value']
        if i['name'] == '2nd Row Leg Room':
            legroom_2nd = i['value']
        if i['name'] == 'Cargo Capacity, All Seats In Place':
            cargo_capacity = i['value']
        if i['name'] == 'Manufacturer 0 60mph Acceleration Time (seconds)':
            zero_to_sixty = i['value']
            #else:
            #   print i['name']
### parse text files for the data we want
print "1st head: {} 2nd head: {} 1st leg: {} 2nd leg: {}".format(headroom_1st,headroom_2nd,legroom_1st,legroom_2nd)