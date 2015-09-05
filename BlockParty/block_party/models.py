import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.ForeignKey(User)
	email = models.CharField(max_length=200)
	phone_num = models.CharField(max_length=15)
	street_address = models.CharField(max_length=200)
	city_name = models.CharField(max_length=200)
	state_name = models.CharField(max_length=200)
	zip_code = models.CharField(max_length=10)
	class Meta:
		abstract = True

class CorporateProfile(Profile):
	business_name = models.CharField(max_length=200)
	contact_first = models.CharField(max_length=200)
	contact_last_name = models.CharField(max_length=200)
	contact_title = models.CharField(max_length=200)

class IndividualProfile(Profile):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	

class DateTime(models.Model):
	date = models.DateField(auto_now=False, auto_now_add=False)
	TIME_CHOICES = (('Morning', 'Morning'),('Afternoon', 'Afternoon'),('Evening', 'Evening'),)
	time_of_day = models.CharField(choices=TIME_CHOICES, max_length=100)

class AvailabilityInfo(models.Model):
	user = models.ForeignKey(IndividualProfile)
	date_time = models.ForeignKey(DateTime)

class Event(models.Model):
	create_date = models.DateTimeField('date published')
	business_name = models.CharField(max_length=200)
	street_address = models.CharField(max_length=200)
	city_name = models.CharField(max_length=200)
	state_name = models.CharField(max_length=200)
	zip_code = models.CharField(max_length=10)
	invited_street_address = models.CharField(max_length=200)
	invited_city_name = models.CharField(max_length=200)
	invited_state_name = models.CharField(max_length=200)
	invited_zip_code = models.CharField(max_length=10)
	radius = models.IntegerField()
	min_attendance = models.IntegerField()
	confirmed_time = models.DateTimeField(auto_now=False, auto_now_add=False)
	def is_public(self):
		return (self.radius or self.invited_street_address)

class Invite(models.Model):
	event = models.ForeignKey(Event)
	invitee = models.ForeignKey(IndividualProfile)
	ATTENDANCE_CHOICES = (('Yes', 'Yes'),('No', 'No'),('Waiting', 'Waiting'),)
	confirmed = models.CharField(choices=ATTENDANCE_CHOICES, max_length=100)



