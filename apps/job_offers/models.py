from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class job_offer(models.Model):
    job_title =  models.CharField(max_length=100)  
    company = models.CharField(max_length=100)  
    city = models.CharField(max_length=200) 
    salary =  models.DecimalField(max_digits=10, decimal_places=2, blank=True, null =True) # Deposito
    user = models.OneToOneField(User, primary_key=True, null=False, on_delete=models.CASCADE)
	
    def __str__(self):
        return ' job_title @{}  user {}'.format(self.job_title, self.user)




