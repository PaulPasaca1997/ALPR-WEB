
from re import template
from django.urls import path, include
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView

from . import views
 

urlpatterns = [
    path('', views.principal, name='principal'),    
   # path('', LoginView.as_view(template_name='login.html'), name='login'),    
    path('administrador/administracion/', views.administracion, name='administracion'),   
    
    path('registro/', views.registroUsuario, name="registro"),
	path('loginA/', views.loginPageA, name="loginA"),  
 	path('loginU/', views.loginPageU, name="loginU"),  
    path('logout/', views.logoutUser, name="logout"),

    #path('usuario', views.usuario, name='usuario'),    
    #path('<int:id>/', views.usuario, name='usuario_edit'),    
    #path('lista/', views.lista, name='lista'),
    #path('eliminar/<int:id>/', views.eliminar, name='usuario_delete'),    
    #path('listaplaca/', views.listaPlaca, name='listaPlaca'),
   

  

]
