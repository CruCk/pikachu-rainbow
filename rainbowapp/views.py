from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from forms import CustomerDetails
from django.http import HttpResponseRedirect,HttpResponse
from forms import CustomerDetailsForm
from django.template import RequestContext

# Create your views here.
def home(request):
	args = {}
	args.update(csrf(request))
	return render_to_response('index.html',args)
def login(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('login.html',args)
def login_check(request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	print username
	print password
	try:
		user = CustomerDetails.objects.get(email=username)
	except CustomerDetails.DoesNotExist:
		return HttpResponseRedirect('/pikachu')
	if user is not None:
		if user.password == password:
			request.session['name'] = username
			return render_to_response('profile.html',{'username' : user.username})
		else:
			html = "<html><body>Password Error</body></html>"
			return HttpResponse(html)
	else:
		html = "<html><body>username Error</body></Html>"
		return HttpResponse(html)
def registration(request):
    args = {}
    args.update(csrf(request))
    return render_to_response('registration.html',args)
def registration_check(request):
    form = CustomerDetailsForm()
    
    print "*********8"
    # print request
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
def profile(request):
	return render_to_response('profile.html')
def logout(request):
	return render_to_response('home.html')
def forgotpwd(request):
	return render_to_response('forgotdetails.html')