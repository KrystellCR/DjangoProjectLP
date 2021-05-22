from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

# Register your models here.

class candidateAdmin(admin.ModelAdmin):
	list_display=(
		'email',
		'created_by',
		'first_name',
		'last_name',
		'avatar',
        'cv',
	)

	list_filter =(
		'created_by',
	)

	search_fields=(
		'email',
	)



admin.site.register(candidate,candidateAdmin)


class invitationAdmin(admin.ModelAdmin):
	list_display=(
		'candidate',
		'link',
		'job_offer',
		'acepted',
		
	)

	list_filter =(
		'job_offer',
	)

	search_fields=(
		'candidate',
	)



admin.site.register(invitation,invitationAdmin)
