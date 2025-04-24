from django.contrib import admin
from django.urls import path, include
from nueva_app.views import home
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nueva_app.urls')),
]
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT )
handler404 = 'nueva_app.views.custom_404'
handler403 = 'nueva_app.views.custom_403'
handler500 = 'nueva_app.views.custom_500'
#handler400 = 'nueva_app.views.custom_400'
