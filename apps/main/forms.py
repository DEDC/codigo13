# Django
from django import forms
from apps.main.models import Artistas


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artistas
        fields = '__all__'
        widgets = {
            'descripcion': forms.Textarea(attrs = {'class': 'materialize-textarea'})
        }