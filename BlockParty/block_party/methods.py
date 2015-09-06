from .models import Event, Invite
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect
#from .models import 
from django.core.urlresolvers import reverse

def get_event(event_id):
	return get_object_or_404(Event, pk=int(event_id))

def get_confirmed_count(event_id):
	return Invite.objects.filter(event=event_id, confirmed='Yes').count()

def get_invited_count(event_id):
	return Invite.objects.filter(event=event_id).count()