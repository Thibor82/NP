from nuevo_proyecto.urls import path, include
from . import views
from .views import PostListView, PostCreateView, PostDetailView

urlpatterns = [
    path('', views.home, name='home' ),
    path('login/', views.loginView, name='login'),
    path('registro/', views.registroView, name='registro'),
    path('logout/', views.logoutView, name='logout'),
    path('post/', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('new/', PostCreateView.as_view(), name='post_create')
]
