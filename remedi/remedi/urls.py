"""
URL configuration for remedi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
# from django.conf.urls.static import static
# from . import settings
# from app.views import Home, Signup_Option, PSignup, DoctorSignup, Login, logout


from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.views import Home, Options, PSignup, DoctorSignup, Login, logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='homepage'),
    path('signupoption/', Options.as_view(), name='signup_option'),
    path('signup/', PSignup.as_view(), name='patient_signup'),
    path('doctor/signup/', DoctorSignup.as_view(), name='doctor_signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
