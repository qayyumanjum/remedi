from django.urls import path
from . import views

urlpatterns = [
    path('generate_key/', views.generate_key_view, name='generate_key'),
    path('encrypt/', views.encrypt_view, name='encrypt'),
    path('decrypt/', views.decrypt_view, name='decrypt'),
]