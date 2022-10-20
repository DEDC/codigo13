# Django
from django.urls import path
from apps.admin.views import CreateArtist, ListArtists, Admin, LoginUser, LogoutUser

app_name = 'admin'

urlpatterns = [
    path('', Admin.as_view(), name='home'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', LogoutUser.as_view(), name='logout'),
    path('artistas/listar', ListArtists.as_view(), name='list_artist'),
    path('artistas/crear', CreateArtist.as_view(), name='create_artist')
]