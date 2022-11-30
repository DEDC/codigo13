# Django
from django import forms
from apps.main.models import Artistas, Eventos


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artistas
        fields = '__all__'
        widgets = {
            'descripcion': forms.Textarea(attrs = {'class': 'materialize-textarea'})
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Eventos
        fields = '__all__'