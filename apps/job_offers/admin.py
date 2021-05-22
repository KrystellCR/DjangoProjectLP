from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

# Register your models here.

class job_offerAdmin(admin.ModelAdmin):
	list_display=(
		'job_title',
		'company',
		'city',
		'salary',
		'user',
	)

	list_filter =(
		'user',
	)

	search_fields=(
		'job_title',
	)



admin.site.register(job_offer,job_offerAdmin)
