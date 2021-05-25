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
        offer =  get_object_or_404(job_offer,id = self.data['job_offer'])
        can = candidate.objects.create(**data)
        can.save()
    
        data_invitation = {
            'candidate': can,
            'link': str(offer.id) +"_" + offer.job_title + "_candidate=" + str(can.id) + "_cand_nom=" + can.first_name,
            'job_offer': offer,
        } 

        inv = invitation.objects.create(**data_invitation)

        return can 
        
       

class aceptedInvitationForm(forms.Form):
    """Sign up form."""

    id_invitation = forms.CharField(min_length=1, max_length=50)
	
    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        inv = get_object_or_404(invitation,id = self.data['id_invitation'])
        inv.acepted = True
        inv.save()
        return inv

        
       
          
       
     

 
  
