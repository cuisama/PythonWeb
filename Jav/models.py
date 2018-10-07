from django.db import models

# Create your models here.
from django.db.models import CharField, TextField, IntegerField


class Video(models.Model):

    id = IntegerField()
    title = TextField()
    url = CharField(max_length=60)
    number = CharField(max_length=10)
    date = CharField(max_length=20)
    length = CharField(max_length=5)
    director = TextField()
    maker = TextField()
    label = TextField()
    review = CharField(max_length=5)
    genres = TextField()
    cast = TextField()