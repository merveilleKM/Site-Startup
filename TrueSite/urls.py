from django.contrib import admin
from django.urls import path
from siteApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('apropos', views.apropos, name='about'),
    path('contact', views.contact, name='contact'),
    path('service', views.service, name='service'),
    path('formation', views.formation, name='formation'),
    path('stage', views.stage, name='stage'),
     path("actualite", views.actualite, name="liste_actualites"),
    path("actualites/<int:id>/", views.actualite_detail, name="actualite_detail"),
 ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
