from django import forms
from django.shortcuts import get_object_or_404

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
        can = candidate.objects.create(**data)
        can.save()
        offer =  get_object_or_404(job_offer,id = self.data['job_offer'])
        data_invitation = {
            'candidate': can,
            'link':'random_'+ str(can.id) + can.first_name,
            'job_offer': offer,
        } 
        inv = invitation.objects.create(**data_invitation)

        return can 
        
       
        
       
     

 
  
