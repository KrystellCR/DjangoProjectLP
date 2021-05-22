from django.urls import path
from . import views


urlpatterns = [

    path(
        route='',
        view=views.login_view,
        name='login'
    ),

    path(
        route='logout/',
        view=views.LogoutView.as_view(),
        name='logout'
    ),
   
     path(
        route='home/',
        view=views.HomeAdminView.as_view(),
        name='home'
    ),

     path(
        route='crear_manager/',
        view=views.CreateManager.as_view(),
        name='crearManager'
    ),
   
   

]