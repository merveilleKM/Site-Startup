from django.contrib import admin
from django.urls import path
from siteApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('apropos', views.apropos, name='about'),
    path('contact', views.contact, name='contact'),
    path('service', views.service, name='service'),
    path('formation', views.formation, name='formation'),
    path('stage', views.stage, name='stage'),
 ]
