from django.contrib import admin
from django.urls import path
from accounts import  views
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('admin/', admin.site.urls),
]
