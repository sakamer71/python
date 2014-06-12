__author__ = 'skamer'
import sqlalchemy
print sqlalchemy.__version__
from sqlalchemy import create_engine
#engine = create_engine('postgresql://postgres:postgres@localhost:5432/cars', pool_size=200)
engine = create_engine('postgresql://postgres:C0riant@localhost:5432/cars', pool_size=400)
engine.echo = True

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
#metadata = MetaData(db)

from sqlalchemy import Column, Integer, Enum, String, VARCHAR, ForeignKey, Numeric, DateTime
from sqlalchemy.orm import relationship,backref

class Make(Base):
    __tablename__ = 'make'
    make_id = Column(Integer,primary_key=True)
    make = Column(String)
    make_n = Column(String)

    def __init__(self, make_id, make, make_n):
    #def __init__(self, make, make_n):
        self.make_id = make_id
        self.make = make
        self.make_n = make_n

    def __repr__(self):
        return "<Make{},{},{}>".format(self.make_id, self.make, self.make_n)


class Model(Base):
    __tablename__ = 'model'
    model_id = Column(Integer,primary_key=True)
    model = Column(String)
    model_n = Column(String)
    year = Column(Integer)
    make_id = Column(Integer,ForeignKey('make.make_id'))

    def __init__(self, model_id, model, model_n, year, make_id):
    #def __init__(self, make, make_n):
        self.model_id = model_id
        self.model = model
        self.model_n = model_n
        self.year = year
        self.make_id = make_id

    def __repr__(self):
        return "<Model{},{},{},{},{}>".format(self.model_id, self.model, self.model_n, self.year, self.make_id)


class Styles(Base):
    __tablename__ = 'styles'
    #modelspecs = Table('modelspecs', metadata,
    style_id = Column(Integer,primary_key=True)
    model_id = Column(Integer,ForeignKey("model.model_id"))
    bodytype = Column(String)
    fueltype = Column(String)
    body_size = Column(String)  ## change to enum (compact, subcompact, midsize, etc)
    trim = Column(String)
    year = Column(Integer)
    engine = Column(String)
    eng_cylinder = Column(String)
    eng_displacement = Column(Numeric)
    eng_hp = Column(Integer)
    eng_torque = Column(Integer)
    submodel = Column(String)
    transmission = Column(String)
    doors = Column(Integer)
    drivenwheels = Column(String)
    fabric = Column(String)
    mpg_hwy = Column(Numeric)
    mpg_city = Column(Numeric)
    seating_rows = Column(Integer)
    seats = Column(Integer)
    headroom_1st = Column(Numeric)
    headroom_2nd = Column(Numeric)
    legroom_1st = Column(Numeric)
    legroom_2nd = Column(Numeric)
    cargo_capacity = Column(Numeric)
    price_msrp = Column(Numeric)
    price_invoice = Column(Numeric)
    zero_to_sixty = Column(Numeric)
    '''
    def __init__(self, style_id, model_id, trim):
        self.style_id = style_id
        self.model_id = model_id
        self.trim = trim
    '''
    def __init__(self, style_id, model_id, bodytype_id, fueltype, body_size, trim, year, \
                 engine, eng_cylinder, eng_displacement, eng_hp, eng_torque, submodel, transmission, doors, \
                 drivenwheels,  fabric, mpg_hwy, mpg_city, seating_rows, seats, headroom_1st, headroom_2nd, \
                 legroom_1st, legroom_2nd, cargo_capacity, price_msrp, price_invoice, zero_to_sixty):
        self.style_id = style_id
        self.model_id = model_id
        self.bodytype_id = bodytype_id
        self.fueltype = fueltype
        self.body_size = body_size
        self.trim = trim
        self.submodel = submodel
        self.year = year
        self.engine = engine
        self.eng_cylinder = eng_cylinder
        self.eng_displacement = eng_displacement
        self.eng_hp = eng_hp
        self.eng_torque = eng_torque
        self.transmission = transmission
        self.doors = doors
        self.drivenwheels = drivenwheels
        self.fabric = fabric
        self.mpg_hwy = mpg_hwy
        self.mpg_city = mpg_city
        self.seating_rows = seating_rows
        self.seats = seats
        self.headroom_1st = headroom_1st
        self.headroom_2nd = headroom_2nd
        self.legroom_1st = legroom_1st
        self.legroom_2nd = legroom_2nd
        self.cargo_capacity = cargo_capacity
        self.price_msrp = price_msrp
        self.price_invoice = price_invoice
        self.zero_to_sixty = zero_to_sixty

    def __repr__(self):
        return "<Model{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},>" \
            .format(self.style_id, self.model_id, self.bodytype_id, self.fueltype, \
                                              self.body_size, self.trim, self.submodel, self.year, self.engine, \
                                              self.eng_cylinder, self.eng_displacement, self.eng_hp, self.eng_torque, \
                                              self.transmission, self.doors, self.drivenwheels, self.fabric, \
                                              self.mpg_hwy, self.mpg_city, self.seating_rows, self.seats, \
                                              self.headroom_1st, self.headroom_2nd, self.legroom_1st, \
                                              self.legroom_2nd, self.cargo_capacity, self.price_msrp, \
                                              self.price_invoice, self.zero_to_sixty)

    '''
    def __repr__(self):
        return "<Style{},{},{}>".format(self.style_id,self.model_id,self.trim)

def create_table_model():
    model = Table('model', metadata,
                 Column('model_id',Integer,primary_key=True),
                 Column('model', VARCHAR(40)),
                 Column('model_n', VARCHAR(40)),
                 Column('year', Integer),
                 Column('make_id',Integer,ForeignKey("make.make_id"))
                 )
    model.create()
'''

class Photo(Base):
    __tablename__ = 'photo'
    photo_id = Column(Integer,primary_key=True)
    photo_ext = Column(String)
    photo_int = Column(String)
    style_id = Column(Integer,ForeignKey('styles.style_id'))

    def __init__(self, photo_id, photo_ext, photo_int, style_id):
        self.photo_id = photo_id
        self.photo_ext = photo_ext
        self.photo_int = photo_int
        self.style_id = style_id

    def __repr__(self):
        return "<Photo{},{},{},{}>".format(self.photo_id, self.photo_ext, self.photo_int, self.style_id)


class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer,primary_key=True)
    username = Column(String)
    password = Column(String)
    fname = Column(String)
    lname = Column(String)
    zipcode = Column(Integer)

    def __init__(self, user_id, username, password, fname, lname, zipcode):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.fname = fname
        self.lname = lname
        self.zipcode = zipcode

    def __repr__(self):
        return "<User{},{},{},{},{},{}>".format(self.user_id, self.username, self.password, \
                                             self.fname, self.lname, self.zipcode)


class Search(Base):
    __tablename__ = 'search'
    search_id = Column(Integer,primary_key=True)
    session_id = Column(String)
    user_id = Column(Integer,ForeignKey('user.user_id'))
    searchstring = Column(String)
    searchdate = Column(DateTime)
    result = Column(String)

    def __init__(self, search_id,session_id,user_id,searchstring,searchdate,result):
        self.search_id = search_id
        self.session_id = session_id
        self.user_id = user_id
        self.searchstring = searchstring
        self.searchdate = searchdate
        self.result = result

    def __repr__(self):
        return "<Search{},{},{},{},{},{}>".format(self.search_id,self.session_id,self.user_id,self.searchstring,\
                                                  self.searchdate,self.result)

class Test(Base):
    __tablename__ = 'test'
    id = Column(Integer,primary_key=True)
    name = Column(String)
    color = Column(String)
    number = Column(Integer)

    def __init__(self, id, name, color, number):
    #def __init__(color):
        #def __init__(self, make, make_n):
        self.id = id
        self.name = name
        self.color = color
        self.number = number

    def __repr__(self):
        return "<Test{},{},{},{},{}>".format(self.id, self.name, self.color, self.number)
        #return "<Test{}>".format(self.color)




print Make.__table__
print Make.__mapper__
Base.metadata.create_all(engine)


