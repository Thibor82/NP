from nuevo_proyecto.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('login/', views.loginView, name='login'),
    path('registro/', views.registroView, name='registro'),
    path('logout/', views.logoutView, name='logout')
]