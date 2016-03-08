from django.contrib import admin

# Register your models here.
from .models import CustomerDetails, EmployeeDetails, OrderDetails

class customerDetailsAdmin(admin.ModelAdmin):
	list_display = ('username', 'email', 'mobilenumber')
	search_fields = ['username']

class employeeDetailsAdmin(admin.ModelAdmin):
	list_display = ('empusername', 'empemail', 'empmobilenumber')
	search_fields = ['empusername']

class orderDetailsAdmin(admin.ModelAdmin):
	list_display = ['get_customer','get_employee', ]
	def get_customer(self, obj):
		return obj.customer.username
	get_customer.admin_order_field = 'customer'
	get_customer.short_description = 'Customer username'
	def get_employee(self, obj):
		return obj.employee.empusername
	get_employee.admin_order_field = 'employee'
	get_employee.short_description = 'Employee username'

admin.site.register(CustomerDetails, customerDetailsAdmin)
admin.site.register(EmployeeDetails, employeeDetailsAdmin)
admin.site.register(OrderDetails, orderDetailsAdmin)