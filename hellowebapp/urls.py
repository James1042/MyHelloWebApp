"""hellowebapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from collection import views
# import password stuff
from django.contrib.auth.views import (
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete,
)


urlpatterns = [
    path('', views.index, name='home'),
    path('about/',
	 TemplateView.as_view(template_name='about.html'),
	 name='about'),
    path('contact/',
	 TemplateView.as_view(template_name='contact.html'),
	 name='contact'),
    path('things/<slug>/', views.thing_detail,
	 name='thing_detail'),
    path('things/<slug>/edit/', 
	views.edit_thing, name='edit_thing'),  
    # the new password reset URLs
    path('accounts/password/reset/', password_reset,
       {'template_name': 'registration/password_reset_form.html'},
       name='password_reset'),
    path('accounts/password/reset/done',
       password_reset_done,
       {'template_name': 'registration/password_reset_done.html'},
       name='password_reset_done'),
    path('accounts/password/reset/<uidb64>/<token>/',
       password_reset_confirm,
       {'template_name': 'registration/password_reset_confirm.html'},
       name='password_reset_confirm'),
    path('accounts/password/done/',
       password_reset_complete,
       {'template_name': 'registration/password_reset_complete.html'},
       name='password_reset_complete'), 
    # end password reset URLs
    path('accounts/', include('registration.backends.simple.urls')), 
    path('admin/', admin.site.urls),
]
