from django.shortcuts import render

# Create your views here.
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
from apps.users.models import *
from apps.job_offers.models import *
from apps.candidates.models import *
# Create your views here.
# Create your views here.


class JobOfferAdminDashboardView(LoginRequiredMixin,TemplateView):
	template_name = 'platform/admin_offers_dashboard.html'

	def get_context_data(self, *args, **kwargs):
		""" Retorna el contexto """
		context = super().get_context_data(*args, **kwargs) 
		context['job_offers'] = job_offer.objects.filter().order_by('-id')
		return context

class JobOfferDashboardView(JobOfferAdminDashboardView):
	template_name = 'platform/manager_offers_dashboard.html'


class CreateJobOffer(LoginRequiredMixin,CreateView):
	template_name = 'platform/admin_offers_dashboard.html'
	model = job_offer
	fields = ['job_title', 'company', 'city', 'salary', 'user']

	def form_invalid(self, form):
		data = form.errors 
		return JsonResponse({'status': False, 'message':form.errors}, status=400)
		
	def form_valid(self, form):
		"""Save form data."""
		form.save()
		return HttpResponse(status=200)


class ManagerstatisticsView(LoginRequiredMixin,TemplateView):
	template_name = 'platform/statistics.html'

	def get_context_data(self, *args, **kwargs):
		""" Retorna el contexto """
		context = super().get_context_data(*args, **kwargs) 
		manager = self.kwargs['manager']
		context['managers'] = User.objects.filter(roles__role = 'manager')

		if manager == 00 or manager == 0:
			context['invitations'] = invitation.objects.filter(acepted = True).order_by('job_offer')
		else:
			context['invitations'] = invitation.objects.filter(candidate__created_by= manager, acepted = True).order_by('job_offer')

		print(context['manager'])
		context['base_url'] = self.request.build_absolute_uri(reverse('CandidateInvitation'))
		return context



	




