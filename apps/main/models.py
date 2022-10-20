from django.db import models
from django.utils.text import slugify
from utils.models import ControlInfo, path_image

class Artistas(ControlInfo):
    identifier = 'ART'
    nombre = models.CharField('Nombre del artista', max_length = 100, unique=True)
    descripcion = models.TextField('Descripción')
    imagen = models.ImageField('Imagen', upload_to=path_image)
    precio_hora = models.DecimalField('Precio por hora de servicio', max_digits=8, decimal_places=2, null=True)
    slug = models.SlugField(editable = False, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Artistas, self).save(*args, **kwargs)