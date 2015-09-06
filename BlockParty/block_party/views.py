from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
#from django.utils import simplejson
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Event, Invite, IndividualProfile, CorporateProfile
import methods
import json

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
	return render(request, 'block_party/events.html', {})

@login_required(redirect_field_name='redirect_path')
def event_details(request, event_id):
	context = {}
	context['event'] = methods.get_event(event_id)
	context['confirmed_count'] = methods.get_confirmed_count(event_id)
	context['invite_count'] = methods.get_invited_count(event_id)
	context['confirmed_perc'] = (methods.get_confirmed_count(event_id) / methods.get_invited_count(event_id)) * 100
	return render(request, 'block_party/event_details.html', context)

@login_required(redirect_field_name='redirect_path')
def create_event(request):
	if request.method == "GET":
		print "hello"
		if request.GET.has_key(u'query'):
			print "hello"
			value = request.GET[u'query']
			model_results = IndividualProfile.objects.filter(first_name__contains=value)
			results = [ {x.id :x.first_name,} for x in model_results ]
			json = json.dumps(results)
			return HttpResponse(json, mimetype='application/json')
		else:
			return render(request, 'block_party/create_event.html', {})

	else:
		event = request.POST.get('event_name', False)
		#search = request.POST.get('search_name', False)
		#if search is not False:
			#return render(request, 'block_party/create_event.html', {'first_result':IndividualProfile.objects.filter(first_name__contains=search)[0].first_name})
		#if event is not False:
			#return render(request, 'block_party/index.html')
		return render(request, 'block_party/create_event.html', {})

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

def add_individual(request):
	first_name = request.POST['first_name']
	last_name = request.POST['last_name']
	email = request.POST['email']
	username = email
	street_address = request.POST['street_address']
	city_name = request.POST['city_name']
	state_name = request.POST['state_name']
	zip_code = request.POST['zip_code']
	phone_num = request.POST['phone_num']
	password = request.POST['password']

	u = User.objects.create_user(username, email, password)
	u.first_name = first_name
	u.last_name = last_name
	
	u.save()

	user_id = u.id

	i = IndividualProfile(email=email,phone_num=phone_num,street_address=street_address,city_name=city_name,state_name=state_name,zip_code=zip_code,first_name=first_name,last_name=last_name,user_id=user_id)
	i.save()

	return HttpResponseRedirect(reverse('block_party_app:events'))

def add_corporate(request):
	business_name = request.POST['business_name']
	email = request.POST['email']
	username = email
	phone_num = request.POST['phone_num']
	contact_first = request.POST['contact_first']
	contact_last_name = request.POST['contact_last_name']
	street_address = request.POST['street_address']
	city_name = request.POST['city_name']
	state_name = request.POST['state_name']
	zip_code = request.POST['zip_code']
	password = request.POST['password']

	u = User.objects.create_user(username, email, password)
	u.first_name = business_name
	
	u.save()

	user_id = u.id

	c = CorporateProfile(email=email,phone_num=phone_num,street_address=street_address,city_name=city_name,state_name=state_name,zip_code=zip_code,business_name=business_name,contact_first=contact_first,contact_last_name=contact_last_name,user_id=user_id)
	c.save()

	return HttpResponseRedirect(reverse('block_party_app:create_event'))
