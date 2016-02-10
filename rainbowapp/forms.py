from django import forms
from models import CustomerDetails
class CustomerDetailsForm(forms.ModelForm):
	class Meta:
		model = CustomerDetails
		fields = ['firstname','lastname','username','email','password','mobilenumber','address']