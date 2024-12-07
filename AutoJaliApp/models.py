from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class CarOwners(models.Model):



    fullname = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    #method to save values with fullname
    def __str__(self):
        return self.username

class BreakDownDetails(models.Model):

    fullname = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=50)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    license = models.FileField(upload_to='licenses/')
    insurance = models.FileField(upload_to='insurance/')
    vehicle_model = models.CharField(max_length=50, default='Unknown Model')
    vehicle_number = models.CharField(max_length=50)
    vehicle_registration = models.CharField(max_length=50)
    vehicle_image = models.ImageField(upload_to='vehicle_images/', default='vehicle_images/placeholder.png')



    def __str__(self):
        return self.fullname


 # Replace with the actual user table name

class Order(models.Model):
    fullname = models.CharField(max_length=100, default='Unknown order')  # Link to your customer/user table
    phone = models.CharField(max_length=50 ,default='Unknown phone')
    pickup_location = models.CharField(max_length=255)
    drop_off_location = models.CharField(max_length=255)
    fare= models.CharField(max_length=255 ,default='Unknown fare')
    driver = models.CharField(max_length=100)

    def __str__(self):
        return self.fullname




