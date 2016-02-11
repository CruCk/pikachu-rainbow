from django.db import models

# Create your models here.
class CustomerDetails(models.Model):
<<<<<<< HEAD
	username = models.CharField(max_length=50)
=======
	firstname = models.CharField(max_length=50,blank=False,default=None)
	lastname = models.CharField(max_length=50,blank=False,default=None)
	username = models.CharField(max_length=20, unique=True)

>>>>>>> 0ce826a6534f1f268df92615cad866e8a1bab986
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=20)
	mobilenumber = models.CharField(max_length=15, unique = True)
	address = models.CharField(max_length=500)
