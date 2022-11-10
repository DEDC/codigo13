# Django
from django.views.generic import TemplateView, DetailView, ListView
from apps.main.models import Artistas
from django.db.models import Q


class Home(TemplateView):
    template_name = 'public/index.html'

    def get_context_data(self, **kwargs):
       context = super(Home, self).get_context_data(**kwargs)
       context['artists'] = Artistas.objects.all()
       return context

class Artista(DetailView):
    template_name = 'public/artista.html'
    model = Artistas

class Search(ListView):
    template_name = 'public/search.html'

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        lookup = (Q(nombre__icontains = q) | Q(folio__icontains = q))
        items = Artistas.objects.filter(lookup, activo = True)
        return items
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context