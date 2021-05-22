from django.urls import path
from . import views
 
urlpatterns = [
     path(
        route='crear_candidato/',
        view=views.CreateCandidateView.as_view(),
        name='CreateCandidate'
    ),
   
   
]