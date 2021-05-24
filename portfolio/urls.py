from django.urls import path
from .views import my_site


urlpatterns = [
    path('', my_site, name='home'),
]
