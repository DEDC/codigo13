# Django
from django.views.generic import TemplateView, DetailView
from apps.main.models import Artistas


class Home(TemplateView):
    template_name = 'public/index.html'

    def get_context_data(self, **kwargs):
       context = super(Home, self).get_context_data(**kwargs)
       context['artists'] = Artistas.objects.all()
       return context

class Artista(DetailView):
    template_name = 'public/artista.html'
    model = Artistas