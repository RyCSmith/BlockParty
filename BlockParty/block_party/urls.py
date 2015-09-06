from django.conf.urls import url

from . import views

urlpatterns = [
	#this will process and route any url requets sent to the polls app. 
	#by the time a request gets here, the pattern that sent it here has been removed
	#it will then route the processing of that request to a function in the views.py file for this app
    
    # ex: /
    url(r'^$', views.index, name='index'),
    # ex: /signup
    url(r'^signup/$', views.signup, name='signup'),
    # ex: /create_event
    url(r'^create_event/$', views.create_event, name='create_event'),
    # ex: /events
    url(r'^events/$', views.events, name='events'),
    # ex: /events/<id>
    url(r'^events/(?P<event_id>[0-9]+)/$', views.event_details, name='event_details'),
    # ex: /profile
    url(r'^profile/$', views.profile, name='profile'),
    #authentication
    url(r'^authenticate/$', views.authentication, name='authentication'),
    #add new individual
    url(r'^add_individual/$', views.add_individual, name='add_individual'),
    #add new corporate sponsor
    url(r'^add_corporate/$', views.add_corporate, name='add_corporate')
]