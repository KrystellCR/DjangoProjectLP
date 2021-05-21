from django.urls import path
from . import views


urlpatterns = [

    path(
        route='login/',
        view=views.login,
        name='login'
    ),
   
     path(
        route='home/',
        view=views.HomeAdminView.as_view(),
        name='home'
    ),
   
   

]