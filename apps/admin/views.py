# Django
from django.views.generic import TemplateView


class Admin(TemplateView):
    template_name = 'admin/template/index.html'