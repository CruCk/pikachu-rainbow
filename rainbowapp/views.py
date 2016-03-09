from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from forms import CustomerDetails
from django.http import HttpResponseRedirect,HttpResponse
from forms import CustomerDetailsForm
from django.template import RequestContext
from rainbowapp.models import CustomerDetails, EmployeeDetails, OrderDetails, RegAdmin

# Create your views here.
# This is for Main landing page. i.e. index page
def index(request):
	args = {}
	args.update(csrf(request))
	return render_to_response('index.html',args)

# This is for login page
def login(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('index.html',args)

# This is for validating the login page.
def login_check(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	try:
		user = CustomerDetails.objects.get(username=username)
	except CustomerDetails.DoesNotExist:
		return HttpResponseRedirect('/pikachu')
	if user is not None:
		if user.password == password:
			request.session['name'] = username
			return HttpResponseRedirect('/pikachu/home')
		else:
			html = "<html><body>Password Error</body></html>"
			return HttpResponse(html)
	else:
		html = "<html><body>username Error</body></Html>"
		return HttpResponse(html)

# This is for registration page.
def registration(request):
    args = {}
    args.update(csrf(request))
    request.session['name'] = ''
    return render_to_response('index.html',args)

# This is for Registration checking page
def registration_check(request):
    form = CustomerDetailsForm()
    if request.POST:
        form = CustomerDetailsForm(request.POST)
        name = request.POST.get('mobilenum')
        print name
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/pikachu/login/')
        else:           
            return render_to_response('mytemplate.html',{'form':form})
    return render_to_response('registration.html',{'form':form}, context_instance=RequestContext(request))

# This is for home page when a customer lands
def home(request):
	if request.session['name'] == '':
		return HttpResponseRedirect('/pikachu')
	userDetails = CustomerDetails.objects.get(username=request.session['name'])
	print userDetails.id
	orderDetails = OrderDetails.objects.filter(customer_id=userDetails.id)
	return render_to_response('home.html',{'username' : request.session['name'], 'orderDetails':orderDetails})

# Logout functionality
def logout(request):
	request.session['name'] = ''
	return HttpResponseRedirect('/pikachu')

# forgot password functionality
def forgotpwd(request):
	return render_to_response('forgotdetails.html')

# **********************************************************************************************************
# Regional Admin details
def regAdmin(request):
	args = {}
	args.update(csrf(request))
	return render_to_response('regAdmin.html',args)
# This is for regional Admin login checking
def regAdminCheck(request):
	regAdminusername = request.POST.get('regAdminusername','')
	regAdminpassword = request.POST.get('regAdminpassword','')
	try:
		regAdminuser = regAdmin.objects.get(regAdminusername=regAdminusername)
	except regAdmin.DoesNotExist:
		return HttpResponseRedirect('/pikachu')
	if regAdminuser is not None:
		if regAdminuser.regAdminpassword == regAdminpassword:
			request.session['regAdminname'] = regAdminusername
			return HttpResponseRedirect('/pikachu/regAdminHome')
		else:
			html = "<html><body>Password Error</body></html>"
			return HttpResponse(html)
	else:
		html = "<html><body>username Error</body></Html>"
		return HttpResponse(html)

# This is for regional admin home page
def regAdminHome(request):
	if request.session['regAdminname'] == '':
		return HttpResponseRedirect('/pikachu')
	return render_to_response('regAdminhome.html')