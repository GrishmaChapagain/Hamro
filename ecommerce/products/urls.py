from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from .forms import LoginForm



urlpatterns = [
    path('', views.home),
    path('login/', auth_views.LoginView.as_view(template_name='pr/login.html',authentication_form=LoginForm), name='login'),
    path('registration/', views.CustomerRegistrationView.as_view(),name='customerregistration'),
  
       
] 