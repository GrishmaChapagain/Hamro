from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm



urlpatterns = [
    path('', views.ProductView.as_view(), name='home'),
    path('product-detail/<int:pk>',views.ProductDetailView.as_view(), name='product-detail'),
    path('login/', auth_views.LoginView.as_view(template_name='pr/login.html',authentication_form=LoginForm), name='login'),
    path('registration/', views.CustomerRegistrationView.as_view(),name='customerregistration'),
    path('profile/', views.profile, name='profile'),
    path('Gnts/', views.Gnts, name='Gnts'),
    path('Gnts/<slug:data>', views.Gnts, name='Gntsdata'),

    path('Ldes/', views.Ldes, name='Ldes'),
    path('Ldes/<slug:data>', views.Ldes, name='Ldesdata'),

    path('Brs/', views.Brs, name='Brs'),
    path('Brs/<slug:data>', views.Brs, name='Brsdata'),

    path('Pan/', views.Pan, name='Pan'),
    path('Pan/<slug:data>', views.Pan, name='Pandata'),

    path('Crm/', views.Crm, name='Crm'),
    path('Crm/<slug:data>', views.Crm, name='Crmdata'),

    path('Shirts/', views.Shirts, name='Shirts'),
    path('Shirts/<slug:data>', views.Shirts, name='Shirtsdata'),





    path('passwordchange/', auth_views.PasswordChangeView.as_view(
        template_name='pr/passwordchange.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(
        template_name='pr/passwordchangedone.html'), name='passwordchangedone'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='pr/password_reset.html',
                                                                 form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='pr/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='pr/password_reset_confirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='pr/password_reset_complete.html'), name='password_reset_complete'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
  
       
] 