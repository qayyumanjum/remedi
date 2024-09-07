from django.urls import path
from . import views

urlpatterns = [
    path('generate_key/', views.generate_key_view, name='generate_key'),
    path('encrypt/', views.encrypt_view, name='encrypt'),
    path('decrypt/', views.decrypt_view, name='decrypt'),
    path('payment/', views.payment_view, name='payment'),
    path('create-checkout-session/', views.create_checkout_session, name='create_checkout_session'),
    path('success/', views.success_view, name='success'),
    path('cancel/', views.cancel_view, name='cancel'),
]
