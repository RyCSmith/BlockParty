from django.contrib import admin
from .models import CorporateProfile, IndividualProfile, Event

class CorporateProfileAdmin(admin.ModelAdmin):
	fields = ['user', 'email', 'phone_num']

admin.site.register(CorporateProfile, CorporateProfileAdmin)