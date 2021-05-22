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
        route='panel_managers/',
        view=views.PanelManagers.as_view(),
        name='panel_managers'
    ),

     path(
        route='crear_manager/',
        view=views.CreateManager.as_view(),
        name='crearManager'
    ),

   
   
   

]