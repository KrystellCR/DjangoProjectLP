from django.urls import path
from . import views
 
urlpatterns = [
     path(
        route='crear_candidato/',
        view=views.CreateCandidateView.as_view(),
        name='CreateCandidate'
    ),
    

     path(
        route='invitacion_aceptar/',
        view=views.CandidateInvitationView.as_view(),
        name='CandidateInvitation'
    ),

      path(
        route='aceptar_form_invitation/',
        view=views.AcceptInvitationView.as_view(),
        name='AceptInvitation'
    ),

   
   
]