# Django
from django.views.generic import TemplateView, DetailView
from apps.main.models import Artistas


class Home(TemplateView):
    extra_context = {
        'artists': Artistas.objects.all()
    }
    template_name = 'public/index.html'

class Artista(DetailView):
    template_name = 'public/artista.html'
    model = Artistas