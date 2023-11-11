import peewee
import datetime

from database import db

class Answer(peewee.Model):
    user = peewee.CharField()
    well_being = peewee.IntegerField()
    physical_activity = peewee.IntegerField()
    stress = peewee.IntegerField()
    social_connections = peewee.IntegerField()
    work_and_studying = peewee.IntegerField()
    date = peewee.TimestampField()

    class Meta:
        database = db


db.create_tables([Answer])