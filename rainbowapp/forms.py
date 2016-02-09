from django import forms
from models import CustomerDetails
class CustomerDetailsForm(forms.ModelForm):
	class Meta:
		model = CustomerDetails
		fields = ['username','email','password','mobilenum','address']