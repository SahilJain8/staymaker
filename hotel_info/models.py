from django.db import models

# Create your models here.
from django.db import models


class GoogleData(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    channel = models.CharField(max_length=50)
    hotel_name = models.CharField(max_length=200)
    num_reviews = models.IntegerField()
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2)
    address = models.CharField(max_length=200)
    other_data = models.TextField()
    is_mmt = models.IntegerField()
    is_booking = models.IntegerField()
    is_jd = models.IntegerField()
    is_agoda = models.IntegerField()
    is_cleartrip = models.IntegerField()
    is_goibibo = models.IntegerField()
    date_time = models.DateTimeField()

    class Meta:
        db_table = 'google_data'


class PincodesTable(models.Model):
    district_id = models.AutoField(primary_key=True)
    district = models.CharField(max_length=255)
    pincode = models.IntegerField()
    state = models.CharField(max_length=255)

    class Meta:
        db_table = 'pincodes_table'


class RequestTable(models.Model):
    user_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=255)
    time_of_query = models.DateTimeField()
    status = models.CharField(max_length=20)

    class Meta:
        db_table = 'request_table'


class ScapeHotels(models.Model):
    channel = models.CharField(max_length=50)
    hotel_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    other_data = models.TextField()
    date_time = models.DateTimeField()

    class Meta:
        db_table = 'scape_hotels'


class UserTable(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(unique=True, max_length=254)
    password = models.CharField(max_length=255)
    ph = models.CharField(max_length=20)

    class Meta:
        db_table = 'user_table'
