from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
#from .models import 
from django.core.urlresolvers import reverse

def index(request):
	return HttpResponse("index")

def signup(request):
	return HttpResponse("signup")

def events(request):
	return HttpResponse("events")

def event_details(request, event_id):
	return HttpResponse("event details: " + str(event_id))

def create_event(request):
	return HttpResponse("create_event")

def profile(request):
	return HttpResponse("profile")

