from peewee import *
from datetime import date

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    Personal_ID = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.

class Ort(Model):
    name = CharField(null = True)
    category = CharField(null = True)
    #This could also have a Self Referencing Relationships

    class Meta:
        database = db # this model uses the "people.db" database

class Fahrt(Model):
    Fahrer = ForeignKeyField(Person, backref='fahrer')
    Startort = ForeignKeyField(Ort, backref='startort')
    Zielort = ForeignKeyField(Ort, backref='zielort')
    Mitfahrer = ForeignKeyField(Person, backref='mitfahrer',null = True)

    class Meta:
        database = db # this model uses the "people.db" database

class Ortsverbindungen(Model):
    ErsterOrt = ForeignKeyField(Ort, backref='ersterort')
    ZweiterOrt = ForeignKeyField(Ort, backref='zweiterort')
    Strecke = CharField()

    class Meta:
        database = db # this model uses the "people.db" database

def createperson(name,Personal_ID):
    try:
        a = Person.create(name= name, Personal_ID= Personal_ID)
    except:
        print ("Whatup")

def createplace(name,category):
    try:
        a = Ort.create(name= name, category= category)
    except:
        print ("Whatup")



db.connect()
db.create_tables([Person, Ort, Fahrt, Ortsverbindungen])

# FirstPerson = Person.create(name='Grandma', Personal_ID='Somestuff')
# FirstOrt = Ort.create(name='München', category='City')
# SecondOrt = Ort.create(name='Berlin', category='City')
# Firstfahrt = Fahrt.create(Fahrer=FirstPerson, Startort = FirstOrt, Zielort = SecondOrt )
# #herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
#
# #all Persons namen
# for person in Person.select():
#     print (person.name)
#
# #all Ortsnamen
# for ort in Ort.select():
#     print (ort.name)
