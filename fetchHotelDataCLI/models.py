from django.db import models
from .fields import ImageListField


class Listing(models.Model):
    title = models.CharField(max_length=255)
    rating = models.FloatField()
    location = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    room_type = models.CharField(max_length=255)
    price = models.FloatField()
    images = ImageListField()

    class Meta:
        db_table = 'hotels'  # This specifies the table name
        # Set this to False since we don't want Django to manage migrations for this table
        managed = False
