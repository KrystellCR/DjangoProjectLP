from django.shortcuts import render
#Django
from django.contrib.auth import authenticate, login, logout # para el login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect #para renderizar
from django.contrib.auth.mixins import LoginRequiredMixin #
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView,FormView,UpdateView,TemplateView
# Create your views here.



def login (request):
	email = ""
	username = ""
	password = ""
	return render(request, 'users/login.html', { 'data':'value', })


class HomeAdminView(TemplateView):
	template_name = 'platform/admin_dashboard.html'

