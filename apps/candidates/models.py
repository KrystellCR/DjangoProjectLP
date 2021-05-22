from django.db import models
from django.contrib.auth.models import User
from apps.job_offers.models import * 

# Create your models here.
class candidate(models.Model):
    email = models.EmailField(max_length=100,unique=True) 
    created_by =  models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)  
    last_name = models.CharField(max_length=200) 
    avatar =  models.ImageField(
		upload_to='pictures',
		blank=True,
		null=True
		)
    cv = models.FileField(upload_to='documents',blank=True,null=True)
	
    def __str__(self):
        return ' first_name @{}   creado por{}'.format(self.first_name, self.created_by)


class invitation(models.Model):
    candidate = models.OneToOneField(candidate, null=False, on_delete=models.CASCADE) # No se puede repetir
    link =  models.CharField(max_length=200) 
    job_offer = models.ForeignKey(job_offer, on_delete=models.CASCADE)
    acepted = models.BooleanField(default=False)

    def __str__(self):
        return ' candidate @{}  job_offer {} acepted {}'.format(self.candidate, self.job_offer, self.acepted)

