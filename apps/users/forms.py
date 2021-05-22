from django import forms

# Models
from django.contrib.auth.models import User
from apps.users.models import  Roles

class ManagerForm(forms.Form):    
    
    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    ) 
    password = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.PasswordInput() 
    ) 
    password_confirmation = forms.CharField(
        min_length=5,
        max_length=70,
        widget=forms.PasswordInput()
    )


    def clean_email(self):
        """ Email must be unique """
        email = self.cleaned_data['email']
        email_taken = User.objects.filter(email=email).exists()
        if email_taken:
            raise forms.ValidationError('el email esta en uso.')
            print("username is already in use")
        return email



    def clean(self):
        """Verify password confirmation match."""			
		#super una forma de llamar a clean antes de ser sobre escrito
        data = super().clean()
       
        if ('password') in data.items() and ('password_confirmation') in data.items:
            password = data['password']
            password_confirmation = data['password_confirmation']
        
            if password != password_confirmation:
                #raise forms.ValidationError('La contraseña no coincide')
                self.add_error('password', "La contraseña no coincide")
                print("Password do not match")

        return data


    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        role_user= 'manager'# Toma el role_user que se mando desde el template
        data.pop('password_confirmation')
        data['username'] = data['email']
        user = User.objects.create_user(**data) # Se genera el usuario
        roles = Roles(user=user)  # Se genera el objeto role en el modelo Roles
        roles.role= role_user     # Se agrega el campo role 
        roles.save()
