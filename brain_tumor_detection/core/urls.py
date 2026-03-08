from django.urls import path
from . import views
from django.urls import path, include
from accounts.views import signup
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('predict/', views.predict, name='predict'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('my-predictions/', views.my_predictions, name='my_predictions'),
    path('dashboard/', views.dashboard, name='dashboard'),


]
