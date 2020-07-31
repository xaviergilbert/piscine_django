from django.urls import path
from . import views

app_name = 'ex00'
urlpatterns = [
    path('', views.acceuil, name='acceuil'),
    path('connexion/', views.connexion, name='connexion'),
	path('inscription/', views.inscription, name='inscription'),
	path('logout/', views.logout, name='logout'),
]