from django import forms

# Models
from django.contrib.auth.models import User
from apps.candidates.models import  *
from apps.job_offers.models import  *

class createCandidateForm(forms.ModelForm):
    """Note model form."""
	#configuracion de la clase
    class Meta:
        """Form settings."""

        model = candidate
        fields = '__all__'
        job_offer = forms.CharField(required=True)


    def save(self):
        """Create Note and modify review_date"""
        data = self.cleaned_data
        data.pop('job_offer')
        candidate = candidate.objects.create(**data)
        candidate.save()
        data_invitation = {
            'candidate': candidate.id,
            'link':'random_'+candidate.id+candidate.first_name,
            'job_offer': job_offer,
        } 
        invitation = invitation.objects.create(**data_invitation)

        return candidate 
        
       
        
       
     

 
  
