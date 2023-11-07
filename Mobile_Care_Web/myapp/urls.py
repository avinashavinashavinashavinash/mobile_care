from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('registration', views.registration),
    path('loginn', views.loginn),
    path('add_customer', views.add_customer),
    path('service', views.service),
    path('search_deatails', views.search_deatails),
    path('delete_service/<int:pk>', views.delete_service,name='delete_service'),
    path('delete_search_service/<int:pk>', views.delete_search_service,name='delete_search_service'),
    path('logout_data', views.logout_data,name='logout_data'),
    path('update_details/<int:id>', views.update_details,name='update_details'),
]