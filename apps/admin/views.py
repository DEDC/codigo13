# Django
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
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

    def form_valid(self, form):
        form.instance.data = {'dates': self.request.POST.get('dates', '').replace(" ", "").split(',')}
        return super().form_valid(form)

class UpdateArtist(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Artistas
    form_class = ArtistForm
    template_name = 'admin/bandas/editar.html'
    success_message = 'Artista editado existosamente'
    login_url = reverse_lazy('admin:login')

    def form_valid(self, form):
        form.instance.data = {'dates': self.request.POST.get('dates', '').replace(" ", "").split(',')}
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('admin:edit_artist', kwargs = {'slug': self.object.slug})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dates'] = []
        data = self.object.data
        if isinstance(data, dict):
            dates = data.get('dates', [])
            context['dates'] = dates
        return context

class ListArtists(LoginRequiredMixin, ListView):
    model = Artistas
    template_name = 'admin/bandas/listar.html'
    login_url = reverse_lazy('admin:login')