__author__ = 'skamer'


f=open('makes.txt','r')
f = f.read()
dict = eval(f)

print dict
for key in dict:
    print key

for makes in dict['makes']:
    print makes['name'], makes['niceName'], makes['id']

#for models in dict['makes']['Nissan']:
 #   print models

def print_data(data):
    # Iterate over the list of all Makes
    for make in data['makes']:

        # A Make, has an: id, name, niceName, and a list of models
        for key, value in make.items():
            # Just print the name & id
            if key == "name":
                print("Name: {0}".format(value))
            elif key == "id":
                print("ID: {0}".format(value))

            # niceName is just a lowercase version of name, so don't
            # do anything...
            elif key == "niceName":
                pass

            # Now, we have a list of models. Iterate over it and
            # print some stuff.
            elif key == "models":
                # It's nice to know how many...
                print("There are {0} models:".format(len(value)))

                # Each model is a dict with an id, name, NiceName, years
                for d in value:
                    # Just pull the years out of the list of years, and
                    # store them as a comma-separated string, e.g.
                    # 2012, 2013, 2014

                    years = ', '.join([
                        str(years['year']) for years in d['years']
                    ])

                    print(" - [{id}, {nice}] {name}. {years}".format(
                        id=d['id'],
                        nice=d['niceName'],
                        name=d['name'],
                        years=years
                    ))

        # print a speparator between each make
        print("-" * 50)

print_data(dict)