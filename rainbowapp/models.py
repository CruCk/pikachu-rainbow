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


class EmployeeDetails(models.Model):
	FIELDS = (
	('ELECT', 'electrician'),
	('CLEAN','cleaning'),
	('PLUMB','plumbing'),
	('LECTR','electronics'),
	)
	empfirstname = models.CharField(max_length=50,blank=False,default=None)
	emplastname = models.CharField(max_length=50,blank=False,default=None)
	empusername = models.CharField(max_length=20, unique=True)
	empemail = models.EmailField(unique=True)
	emppassword = models.CharField(max_length=20)
	empmobilenumber = models.CharField(max_length=15, unique = True)
	empaddress = models.CharField(max_length=500)
	empfield = models.CharField(max_length=5, choices=FIELDS)

class OrderDetails(models.Model):
	customer = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE)
	employee = models.ForeignKey(EmployeeDetails, on_delete=models.CASCADE)
	customerRating = models.IntegerField(default=0)
	employeeRating = models.IntegerField(default=0)
	


