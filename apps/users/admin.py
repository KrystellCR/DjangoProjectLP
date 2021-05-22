from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User



# Register your models here.
@admin.register(Roles)
class RolesAdmin(admin.ModelAdmin):
	#raw_id_fields = ['user',]
	list_display = (
		'user','role',
	)
	list_filter =(
		'role',
	)