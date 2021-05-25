from django.shortcuts import render
from django.contrib.auth.models import User
#Django
from django.contrib.auth import authenticate, login, logout # para el login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect #para renderizar
from django.contrib.auth.mixins import LoginRequiredMixin #
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView,FormView,UpdateView,TemplateView,CreateView
from django.http import JsonResponse
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
#forms 
from apps.users.forms import ManagerForm
from apps.users.models import *
from apps.job_offers.models import *
# Create your views here.



def login_view (request):
	email = ""
	username = ""
	password = ""
	value = ""
	print("On Login")
	if request.method == "POST":
		email = request.POST.get('email','')
		password = request.POST.get('password','')

		if User.objects.filter(email=email).exists() == True : # si el email exite 
			username = User.objects.get(email=email).username		
			print("Username*******:", username)
			user= authenticate(request,username=username,password=password)
				
			if user:	# Si hay un user entonces va a generar la sesion
				login(request,user)
				if user.is_staff:
					return redirect('/usuario/panel_managers/')	
				else:
					return redirect('/oferta_de_trabajo/panel_manager')	
						
		else:
			value = "Correo o contraseña incorrecta"
			print("Incorrecto")
			return render(request, 'users/login.html', { 'data': value, })
					
	return render(request, 'users/login.html', { 'data': value, })


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""
    template_name = 'users/login.html'
	

class PanelManagers(LoginRequiredMixin,TemplateView):
	template_name = 'platform/admin_dashboard.html'

	def get_context_data(self, *args, **kwargs):
		""" Retorna el contexto """
		context = super().get_context_data(*args, **kwargs) 
		context['managers'] = User.objects.filter(roles__role='manager').order_by('-id')
		return context


class CreateManager(LoginRequiredMixin,FormView):
	template_name = 'platform/admin_dashboard.html'
	form_class = ManagerForm 

	def form_invalid(self, form):
		data = form.errors 
		return JsonResponse({'status': False, 'message':form.errors}, status=400)
		
	def form_valid(self, form):
		"""Save form data."""
		print("Creo usuario exitosamente")
		form.save()
		return HttpResponse(status=200)



