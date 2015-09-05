from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
#from .models import 
from django.core.urlresolvers import reverse

def index(request):
	return render(request, 'block_party/index.html', {})

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

