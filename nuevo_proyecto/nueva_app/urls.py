from nuevo_proyecto.urls import path, include
from . import views
from .views import PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView






urlpatterns = [
    path('', views.home, name='home' ),
    path('login/', views.loginView, name='login'),
    path('registro/', views.registroView, name='registro'),
    path('logout/', views.logoutView, name='logout'),
    path('post/', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('new/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]

# urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)