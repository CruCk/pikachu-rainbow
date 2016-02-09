from django.db import models

# Create your models here.
class CustomerDetails(models.Model):
	username = models.CharField(max_length=50)
	
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=20)
	mobilenum = models.CharField(max_length=15)
	address = models.CharField(max_length=500)
