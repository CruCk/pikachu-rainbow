from django import forms
from models import CustomerDetails
from models import EmployeeDetails
class CustomerDetailsForm(forms.ModelForm):
	class Meta:
		model = CustomerDetails
		fields = ['firstname','lastname','username','email','password','mobilenumber','address']

