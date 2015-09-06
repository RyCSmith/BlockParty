from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
#from .models import 
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
	if request.user.is_authenticated():
		context = {'loggedin':True,'first_name':request.user.first_name}
	else:
		context = {'loggedin':False}
	return render(request, 'block_party/index.html', context)

def signup(request):
	return render(request, 'block_party/signup.html')

@login_required(redirect_field_name='redirect_path')
def events(request):
	return HttpResponse("events")

@login_required(redirect_field_name='redirect_path')
def event_details(request, event_id):
	new = int(event_id)
	return render(request, 'block_party/index.html', {'event_id':new})

@login_required(redirect_field_name='redirect_path')
def create_event(request):
	return HttpResponse("create_event")

@login_required(redirect_field_name='redirect_path')
def profile(request):
	return HttpResponse("profile")

"""Uses POST form data to attempt to authenticate the user. If authentication succeeds, checks if user
was rerouted from page requiring authentication and redirects there. If not redirects to events page. If
authentication fails, redirects to homepage."""
def authentication(request):
	email = request.POST.get('user_email', False)
	password = request.POST.get('user_password', False)
	user = authenticate(username=email, password=password) 
	redirect_path = request.POST.get('redirect_path', False)
	if user is not None:
		login(request, user)
		if redirect_path != 'False':
			full_path = 'block_party_app:' + redirect_path
			full_path = full_path.replace("/", "")
			return HttpResponseRedirect(reverse(full_path))
		return HttpResponseRedirect(reverse('block_party_app:events'))
	else:
		return HttpResponseRedirect(reverse('block_party_app:index'))

"""Processes POST request from user requesting log out. Redirects to the home page."""
def logout_command(request):
	logout(request)
	return HttpResponseRedirect(reverse('block_party_app:index'))

"""Returns a view of a page telling user login is required. If user was rerouted from page
requiring authentication, redirect_path is added to the POST data that will be submitted with authentication request."""
def login_page(request):
	return render(request, 'block_party/login.html', {'redirect_path' : request.GET.get('redirect_path', False)})
