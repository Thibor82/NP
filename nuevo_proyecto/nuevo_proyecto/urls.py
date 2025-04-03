from django.contrib import admin
from django.urls import path, include
from nueva_app.views import home
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nueva_app.urls')),
]
