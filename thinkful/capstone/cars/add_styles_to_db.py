__author__ = 'skamer'
from create_db_new import *
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
print "Querying the db now.................."
for i in session.query(Model).filter(Model.model_n=='mazda6'):
#for i in session.query(Model):
    mymodel = i.model
    mymodeln = i.model_n
    mymodelid = i.model_id
    print "Model name is {} and formal is {} and model id is {}".format(mymodeln, mymodel, mymodelid)

#exit()

for i in session.query(Make):
    mymake = i.make

    import pprint
    #mymake = 'mazda'
    #mymake = 'tesla'
    f = open('data/makes/{}_models.txt'.format(mymake), 'r')
    dict = eval(f.read())
    for key in dict:
        if key =='modelsCount':
            myrange = int(dict[key])
            print "the modelscount for {} is {}".format(mymake,myrange)

#    for i in range(myrange):  ## the range of models from the json in {make}_models.txt
 #       print dict['models'][i]['id'], dict['models'][i]['name'], dict['models'][i]['niceName'], dict['models'][i]['years'][0]['id']


  #  print dict['models'][6]['id'], dict['models'][i]['name'], dict['models'][i]['niceName']

    print '---------'
    num_models = len(dict['models'])
    print "there are {} models for {}".format(num_models, mymake)
    for model in range(num_models):
        modelnicename = dict['models'][model]['niceName']
        print "Model {}: ".format(modelnicename)
        stuff = dict['models'][model]['years'][0]
        mylen = len(stuff['styles'])
        for i in range(mylen):
            print '\tStyle Name: ', stuff['styles'][i]['name']  ##trim
            mytrim = stuff['styles'][i]['name']
            print '\tStyle ID: ', stuff['styles'][i]['id']  ## style_id
            mystyleid = stuff['styles'][i]['id']
            for i in session.query(Model).filter(Model.model_n==modelnicename):
                mymodelid = int(i.model_id)

            #print '\tHITHERE  ', i.model_id
                print '\tModel ID:  ', mymodelid  ##model_id
                newstyle = Styles(style_id = mystyleid, trim = mytrim, model_id = mymodelid )  ## create new row to add to db
                session = Session()
                ##### Write to make table of cars db
                session.add(newstyle)
                session.commit()
                session.close()
    ## how many distinct styles do i have?
    #mylist = [2,4,3,5,6,7,1]
    mylen = len(stuff['styles'])
    print "list length is {}".format(mylen)

    print stuff['styles']

    pp = pprint.PrettyPrinter(indent=2)
    #pp = pprint.pprint(dict)