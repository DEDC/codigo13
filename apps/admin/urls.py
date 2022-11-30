# Django
from django.urls import path
from apps.admin.views import CreateArtist, ListArtists, Admin, LoginUser, LogoutUser, UpdateArtist, ListEvents, HideArtist

app_name = 'admin'

urlpatterns = [
    path('', Admin.as_view(), name='home'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', LogoutUser.as_view(), name='logout'),
    path('artistas/listar', ListArtists.as_view(), name='list_artist'),
    path('artistas/crear', CreateArtist.as_view(), name='create_artist'),
    path('eventos/listar', ListEvents.as_view(), name='list_events'),
    path('artista/<slug:slug>/editar', UpdateArtist.as_view(), name='edit_artist'),
    path('artista/<int:pk>/ocultar', HideArtist.as_view(), name='hide_artist')
]