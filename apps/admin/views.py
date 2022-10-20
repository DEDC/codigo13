# Django
from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from apps.main.models import Artistas
from apps.main.forms import ArtistForm


class Admin(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('admin:login')
    template_name = 'admin/home.html'

class LoginUser(LoginView):
    template_name = 'admin/login.html'
    next_page = reverse_lazy('admin:home')

class LogoutUser(LogoutView):
    next_page = reverse_lazy('admin:login')

class CreateArtist(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Artistas
    form_class = ArtistForm
    template_name = 'admin/bandas/registro.html'
    success_url = reverse_lazy('admin:create_artist')
    success_message = 'Artista registrado existosamente'
    login_url = reverse_lazy('admin:login')

class ListArtists(LoginRequiredMixin, ListView):
    model = Artistas
    template_name = 'admin/bandas/listar.html'
    login_url = reverse_lazy('admin:login')