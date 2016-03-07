from django.contrib import admin

# Register your models here.
from .models import CustomerDetails, EmployeeDetails, OrderDetails

admin.site.register(CustomerDetails)
admin.site.register(EmployeeDetails)
admin.site.register(OrderDetails)