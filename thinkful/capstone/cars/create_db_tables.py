__author__ = 'skamer'
from sqlalchemy import *

db = create_engine('postgresql://postgres:C0riant@localhost:5432/cars')
db.echo = True
metadata = MetaData(db)
conn = db.connect()
#create = 0
#drop = 1

droptables=['searches', 'users', 'photo', 'modelspecs', 'model', 'make', 'bodytype']
types = ['fuel_types','drive_types','transmission_types']

def create_table_make():
    make = Table('make', metadata,
                  Column('make_id',Integer,primary_key=True),
                  Column('make', VARCHAR(40)),
                  Column('make_n', VARCHAR(40)),
                  )
    make.create()

def create_table_model():
    model = Table('model', metadata,
                 Column('model_id',Integer,primary_key=True),
                 Column('model', VARCHAR(40)),
                 Column('model_n', VARCHAR(40)),
                 Column('year', Integer),
                 Column('make_id',Integer,ForeignKey("make.make_id"))
                 )
    model.create()

def create_table_bodytype():
    bodytype = Table('bodytype', metadata,
                Column('bodytype_id',Integer,primary_key=True),
                Column('bodytype', VARCHAR(40))
                )
    bodytype.create()

def create_table_fueltype():
    fueltype = Table('fueltype', metadata,
                     Column('fueltype_id',Integer,primary_key=True),
                     Column('fueltype', VARCHAR(40))
                )
    fueltype.create()

def create_table_modelspecs():
    modelspecs = Table('modelspecs', metadata,
                 Column('style_id',Integer,primary_key=True),
                 Column('model_id',Integer,ForeignKey("make.make_id")),
                 Column('bodytype_id',Integer,ForeignKey("bodytype.bodytype_id")),
                 Column('fueltype_id',Enum('gas','diesel','hybrid','electric',name='fuel_types')),
                 Column('body_size', VARCHAR(40)),  ## change to enum (compact, subcompact, midsize, etc)
                 Column('trim', VARCHAR(40)),
                 Column('submodel', VARCHAR(40)),
                 Column('year', Integer),
                 Column('engine', VARCHAR(40)),
                 Column('eng_cylinder', VARCHAR(40)),
                 Column('eng_displacement', Integer),
                 Column('eng_hp', Integer),
                 Column('eng_torque', Integer),
                 Column('transmission', Enum('manual','automatic',name='transmission_types')),
                 Column('doors', Integer),
                 Column('drivenwheels', Enum('front','rear','AWD','4WD',name='drive_types')),
                 Column('fabric', VARCHAR(40)),
                 Column('mpg_hwy', Integer),
                 Column('mpg_city', Integer),
                 Column('seating_rows', Integer),
                 Column('seats', Integer),
                 Column('headroom_1st', Integer),
                 Column('headroom_2nd', Integer),
                 Column('legroom_1st', Integer),
                 Column('legroom_2nd', Integer),
                 Column('cargo_capacity', Integer),
                 Column('price_msrp', Integer),
                 Column('price_invoice', Integer),
                )
    modelspecs.create()

def create_table_photo():
    photo = Table('photo', metadata,
            Column('photo_id',Integer,primary_key=True),
            Column('style_id',Integer,ForeignKey("modelspecs.style_id")),
            Column('photo_name', VARCHAR(40)),
            Column('photo_url_full', VARCHAR(120)),
            Column('photo_url_base', VARCHAR(120)),
            Column('photo_url_uri', VARCHAR(120)),
            )
    photo.create()

def create_table_users():
    users = Table('users', metadata,
                  Column('user_id',Integer,primary_key=True),
                  Column('username', VARCHAR(15)),
                  Column('firstname', VARCHAR(15)),
                  Column('lastname', VARCHAR(15)),
                  Column('zipcode', Integer),
                  Column('password', VARCHAR(15)),
                  Column('email', VARCHAR(80)),
                  Column('openid', VARCHAR(120)),
                  )
    users.create()

def create_table_searches():
    searches = Table('searches', metadata,
                  Column('search_id',Integer,primary_key=True),
                  Column('search_kw', VARCHAR(120)),
                  Column('user_id', Integer,ForeignKey("users.user_id")),
                  Column('search_string', VARCHAR(1024)), ##dictionary or json of all search params
                  Column('date', DateTime),
                  Column('results', VARCHAR(1024)),  ##dictionary of styleids + percentmatch
                  )
    searches.create()


def drop_tables(tables):
    for table in tables:
        print "now dropping table: {}".format(table)
        mytable = Table(table,metadata, autoload = True)
        mytable.drop()
    ## adding to manually drop the Types (enum) b/c it isnt working via the above now.

def drop_types(types):
    for type in types:
        print "Dropping type: {}".format(type)
        sql = 'drop type {} cascade;'.format(type)
        conn.execute(sql)
    conn.close()



##create tables
def main(action):
    if action == 'create':
        create_table_make()
        create_table_model()
        create_table_bodytype()
        create_table_modelspecs()
        create_table_photo()
        create_table_users()
        create_table_searches()
    elif action == 'delete':
        drop_tables(droptables)
        drop_types(types)
    else:
        print "Enter create or delete"

## main
#main('create')
main('delete')
