from django.db import models

# Create your models here.
class CustomerDetails(models.Model):
	firstname = models.CharField(max_length=50,blank=False,default=None)
	lastname = models.CharField(max_length=50,blank=False,default=None)
	username = models.CharField(max_length=20, unique=True)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=20)
	mobilenumber = models.CharField(max_length=15, unique = True)
	address = models.CharField(max_length=500)
