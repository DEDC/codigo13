# Django
from django.views.generic import TemplateView, DetailView, ListView, CreateView
from apps.main.models import Artistas, Eventos
from apps.main.forms import EventForm
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib import messages

class Home(TemplateView):
    template_name = 'public/index.html'

    def get_context_data(self, **kwargs):
       context = super(Home, self).get_context_data(**kwargs)
       context['artists'] = Artistas.objects.filter(activo=True)
       return context

class Artista(DetailView):
    template_name = 'public/artista.html'
    model = Artistas

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dates'] = []
        data = self.object.data
        if isinstance(data, dict):
            dates = data.get('dates', [])
            context['dates'] = dates
        return context
    
    def post(self, *args, **kwargs):
        form = EventForm(self.request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.artista = self.get_object()
            f.save()
            messages.success(self.request, 'Se ha enviado la información para realizar la contratación')
        else:
            messages.error(self.request, 'No se ha podido completar la acción. Inténtelo de nuevo.')
        return self.get(*args, **kwargs)

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