from django.urls import path
from . import views
 
urlpatterns = [
     path(
        route='',
        view=views.JobOfferAdminDashboardView.as_view(),
        name='JobOfferAdminDashboard'
    ),

    path(
        route='panel_manager',
        view=views.JobOfferDashboardView.as_view(),
        name='JobOfferDashboard'
    ),

    path(
        route='crear_oferta/',
        view=views.CreateJobOffer.as_view(),
        name='createJobOffer'
    ),

     path(
        route='estadisticas_manager/<int:manager>',
        view=views.ManagerstatisticsView.as_view(),
        name='ManagerstatisticsView'
    ),
   
   
]