from django import forms
from models import CustomerDetails, RegAdmin, EmployeeDetails, OrderDetails

class CustomerDetailsForm(forms.ModelForm):
	class Meta:
		model = CustomerDetails
		fields = ['firstname','lastname','username','email','password','mobilenumber','address']

class RegAdminForm(forms.ModelForm):
	class Meta:
		model = RegAdmin
		fields = ['regAdminfirstname','regAdminlastname','regAdminusername','regAdminemail','regAdminpassword','regAdminmobilenumber','regAdminaddress']
