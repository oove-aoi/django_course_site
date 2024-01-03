from django.contrib import admin
from .models import Meetup, Participant, Location
# Register your models here.

class MeetupAdmin(admin.ModelAdmin):
	list_display = ('title', 'date', 'location')
	list_filter = ('date', 'location',)
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(Meetup,MeetupAdmin)
admin.site.register(Participant)
admin.site.register(Location)
