from django.db import models
from django.utils.text import slugify
from utils.models import ControlInfo, path_image
from django.core.validators import RegexValidator

class Artistas(ControlInfo):
    identifier = 'ART'
    nombre = models.CharField('Nombre del artista', max_length = 100, unique=True)
    descripcion = models.TextField('Descripción')
    imagen = models.ImageField('Imagen', upload_to=path_image)
    precio_hora = models.DecimalField('Precio por hora de servicio', max_digits=8, decimal_places=2, null=True)
    data = models.JSONField(null=True, blank=True, default=dict)
    slug = models.SlugField(editable = False, unique=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super(Artistas, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ['fecha_reg']

class Eventos(ControlInfo):
    identifier = 'EVT'
    artista = models.ForeignKey(Artistas, on_delete=models.PROTECT, editable=False)
    fecha = models.DateField()
    hora = models.TimeField()
    descripcion = models.TextField()
    lugar = models.CharField('Lugar del evento', max_length=300)
    nombre_cto = models.CharField('Nombre del contacto', max_length=300)
    telefono_cto = models.CharField('Teléfono del contacto', max_length=10, validators=[RegexValidator('^[0-9]*$', 'Ingrese un número de teléfono correcto')])
    correo_cto = models.EmailField('Correo electrónico del contacto')