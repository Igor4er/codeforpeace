import peewee

from .database import db

class User(peewee.Model):
    email = peewee.CharField(unique=True, index=True)
    hashed_password = peewee.CharField()
    is_active = peewee.BooleanField(default=True)

    class Meta:
        database = db


class Answer(peewee.Model):
    user = peewee.CharField(primary_key=True)
    well_being = peewee.IntegerField()
    physical_activity = peewee.IntegerField()
    stress = peewee.IntegerField()
    social_connections = peewee.IntegerField()
    work_and_studying = peewee.IntegerField()
    date = peewee.DateTimeField()

    class Meta:
        database = db
