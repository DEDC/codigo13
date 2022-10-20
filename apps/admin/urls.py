# Django
from django.urls import path
from apps.admin.views import CreateArtist, ListArtists, Admin

app_name = 'admin'

urlpatterns = [
    path('', Admin.as_view(), name='home'),
    path('artistas/listar', ListArtists.as_view(), name='list_artist'),
    path('artistas/crear', CreateArtist.as_view(), name='create_artist')
]