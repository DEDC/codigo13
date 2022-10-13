from django.db import models
from django.utils.text import slugify
from utils.models import ControlInfo

class Artistas(ControlInfo):
    nombre = models.CharField('Nombre del artista', max_length = 100)
    descripcion = models.TextField('Descripción')
    imagen = models.ImageField('Imagen')
    slug = models.SlugField(editable = False, blank = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Artistas, self).save(*args, **kwargs)