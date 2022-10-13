# Django
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'public/index.html'