# Django
from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from apps.main.models import Artistas
from apps.main.forms import ArtistForm


class Admin(TemplateView):
    template_name = 'admin/home.html'

class CreateArtist(SuccessMessageMixin, CreateView):
    model = Artistas
    form_class = ArtistForm
    template_name = 'admin/bandas/registro.html'
    success_url = reverse_lazy('admin:create_artist')
    success_message = 'Artista registrado existosamente'

class ListArtists(ListView):
    model = Artistas
    template_name = 'admin/bandas/listar.html'