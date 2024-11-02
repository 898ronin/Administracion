# reservations/urls.py
from django.urls import path
from .views import (
    client_list, create_client, update_client, delete_client,
    reservation_list, create_reservation, edit_reservation, delete_reservation,
    department_list, create_department, update_department, delete_department,
    index
)

urlpatterns = [
    path('', index, name='index'),
    # Client URLs
    path('clients/', client_list, name='client_list'),
    path('clients/new/', create_client, name='create_client'),
    path('clients/edit/<int:pk>/', update_client, name='update_client'),
    path('clients/delete/<int:pk>/', delete_client, name='delete_client'),
    # Reservation URLs
    path('reservations/', reservation_list, name='reservation_list'),
    path('reservations/new/', create_reservation, name='create_reservation'),  # Asegúrate que aquí se use el mismo nombre
    path('reservations/edit/<int:reservation_id>/', edit_reservation, name='reservation_edit'),
    path('reservations/delete/<int:reservation_id>/', delete_reservation, name='reservation_delete'),
    # Department URLs
    path('departments/', department_list, name='department_list'),
    path('departments/new/', create_department, name='create_department'),
    path('departments/edit/<int:pk>/', update_department, name='update_department'),
    path('departments/delete/<int:pk>/', delete_department, name='delete_department'),
]
