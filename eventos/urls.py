# Django
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# app main
from apps.main.views import Home, Artista
from apps.admin.views import Admin

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('contratar/<slug:slug>', Artista.as_view(), name='contratar'),
    path('admin/', include('apps.admin.urls', namespace='admin'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)