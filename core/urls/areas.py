from django.urls import path
from core.views.areas import home

urlpatterns = [
    path('', home, name='home'),
]