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
from apps.candidates.forms import createCandidateForm,aceptedInvitationForm
from apps.users.models import *
from apps.candidates.models import * 
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
		self.object = form.save()
		
		link = self.object.invitation.link
		base_url = self.request.build_absolute_uri(reverse('CandidateInvitation'))
		return JsonResponse({'status': False, 'message':link,'base_url':base_url}, status=200)


class CandidateInvitationView(TemplateView):
	template_name = 'platform/candidate_invitation.html'

	def get_context_data(self, *args, **kwargs):
		""" Retorna el contexto """
		context = super().get_context_data(*args, **kwargs) 
		link_invitation =  self.request.GET.get('invitation')
		context['invitation'] = get_object_or_404(invitation, link= link_invitation)
		return context



class AcceptInvitationView(FormView):
	template_name = 'platform/candidate_invitation.html'
	form_class = aceptedInvitationForm 
		
	def form_valid(self, form):
		self.object = form.save()
		return redirect(self.request.META['HTTP_REFERER'])	

	def form_invalid(self, form):
		data = form.errors 
		return JsonResponse({'status': False, 'message':form.errors}, status=400)



