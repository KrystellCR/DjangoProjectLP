from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
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
from apps.candidates.forms import createCandidateForm
from apps.users.models import *
from apps.job_offers.models import *
# Create your views here.
# Create your views here.


class CreateCandidateView(LoginRequiredMixin,CreateView):
	template_name = 'platform/manager_offers_dashboard.html'
	form_class = createCandidateForm

	def post(self, request, *args, **kwargs):
		self.object = None
		return super().post(request, *args, **kwargs)

	def form_invalid(self, form):
		data = form.errors 
		return JsonResponse({'status': False, 'message':form.errors}, status=400)
		
	def form_valid(self, form):
		"""Save form data."""
		form.save()
		return HttpResponse(status=200)


