import contextvars
from multiprocessing import context
from urllib import request
from wsgiref.util import request_uri
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponse
from .forms import login_form
from .models import Pilot
from .models import Airplane
from .models import Employee
from .models import PlaneType

# Create your views here.
def home(request):
    pilot = Pilot.objects.all()
    airplane=Airplane.objects.all()
    employee=Employee.objects.all()
    planetype=PlaneType.objects.all()
    return render(request, 'index.html',{'pilot':pilot,'airplane':airplane,'employee':employee,'planetype':planetype})


#def register(request):
  # return render(request, 'register.html')

def user(request):
   #plots = Plots.objects.all()
   return render(request, 'user.html')

def login(request):
    context={}
    context['form']=login_form()
    return render(request,"login.html",context)  

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect("main:homepage")
		
	form = NewUserForm()
	return render (request=request, template_name="main/register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})
