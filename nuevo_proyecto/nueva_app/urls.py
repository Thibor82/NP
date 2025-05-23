from django.urls import path, include
from . import views
from django.views.generic import RedirectView
from django.templatetags.static import static as static_url
from .views import PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView
from .views import TagListView, TagCreateView, TagDeleteView, PostbyTagView







urlpatterns = [
    path('', views.home, name='home' ),
    
    path('login/', views.loginView, name='login'),
    path('registro/', views.registroView, name='registro'),
    path('logout/', views.logoutView, name='logout'),
    path('post/', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('new/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('tags/', TagListView.as_view(), name='tag_list'),
    path('tags/newtag/', TagCreateView.as_view(), name='tag_create'),
    path('tags/<int:pk>/delete/', TagDeleteView.as_view(), name='tag_delete'),
    path('post_by_tag/<int:pk>/', PostbyTagView.as_view(), name='post_list_by_tag'),
    path('politica-cookies/', views.politica_cookies, name='politica_cookies'),
    path('weather/', views.weather, name ='weather'),
    path('recipe/', views.recipe, name ='recipe'),
]   

# urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


