from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
#from .models import 
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def index(request):
	if request.user.is_authenticated():
		context = {'loggedin':True,'first_name':request.user.first_name}
	else:
		context = {'loggedin':False}
	return render(request, 'block_party/index.html', context)

def signup(request):
	return render(request, 'block_party/signup.html')

def events(request):
	return HttpResponse("events")

def event_details(request, event_id):
	new = int(event_id)
	return render(request, 'block_party/index.html', {'event_id':new})

def create_event(request):
	return HttpResponse("create_event")

def profile(request):
	return HttpResponse("profile")

def authentication(request):
	email = request.POST.get('user_email', False)
	password = request.POST.get('user_password', False)
	user = authenticate(username=email, password=password) 
	if user is not None:
		login(request, user)
		return HttpResponseRedirect(reverse('block_party_app:events'))
	else:
		return HttpResponseRedirect(reverse('block_party_app:index'))

