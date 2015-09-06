from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Event, Invite
import methods

def index(request):
	if request.user.is_authenticated():
		context = {'loggedin':True,'first_name':request.user.first_name}
	else:
		context = {'loggedin':False}
	return render(request, 'block_party/index.html', context)

def signup(request):
	return render(request, 'block_party/signup.html')

def events(request):
	return render(request, 'block_party/events.html', {})

def event_details(request, event_id):
	context = {}
	context['event'] = methods.get_event(event_id)
	context['confirmed_count'] = methods.get_confirmed_count(event_id)
	context['invite_count'] = methods.get_invited_count(event_id)
	context['confirmed_perc'] = (methods.get_confirmed_count(event_id) / methods.get_invited_count(event_id)) * 100
	return render(request, 'block_party/event_details.html', context)

def create_event(request):
	return render(request, 'block_party/create_event.html', {})

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

