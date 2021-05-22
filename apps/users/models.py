from django.db import models
from django.contrib.auth.models import User

class Roles(models.Model):
	user = models.OneToOneField(User, primary_key=True, null=False, on_delete=models.CASCADE)
	role = models.CharField(max_length=25, blank=True)

	def __str__(self):
		""" Return role """	
		return format(self.role)