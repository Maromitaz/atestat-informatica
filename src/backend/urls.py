from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('admin/', admin.site.urls, name="admin"),
	path('', views.index, name="acasa"),
	path('mesaje/', views.mesaje, name="mesaje"),
	path('contact/',views.contact, name="contact"),
	path('showcar/', views.showcar, name="showcar"),
]

handler404 = views.eroare_404