# hotel_management/urls.py
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='reservations/', permanent=False)),  # Redirige la raíz a /reservations/
    path('reservations/', include('reservations.urls')),
]
