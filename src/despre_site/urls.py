from django.urls import path
from . import views

urlpatterns = [ 
    path("",views.despre, name="despre_site"),
    path("unelte_folosite/",views.unelte_folosite, name="unelte_folosite"),
    path("bootstrap/",views.Bootstrap, name="bootstrap"),
    path("django/",views.Django, name="Django"),
    path("ThreeJS/",views.ThreeJS, name="ThreeJS"),
    path("FontAwesome/",views.FontAwesome, name="FontAwesome"),
    path("tema_aleasa/",views.tema_aleasa, name="tema_aleasa"),
    path("HTML/", views.HTML, name="HTML"),
    path("CSS/", views.CSS, name="CSS"),
    path("Javascript/", views.Javascript, name="Javascript"),
    path("Vite/", views.Vite, name="Vite"),
    path("NGINX/", views.NGINX, name="NGINX"),
    path("Docker/", views.Docker, name="Docker"),
]
