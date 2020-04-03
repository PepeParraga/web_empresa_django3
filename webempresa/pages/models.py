from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Pages(models.Model):
    title  = models.CharField(verbose_name='Título',max_length=200)
    content= RichTextField(verbose_name='Contenido')
    order  = models.SmallIntegerField(verbose_name='Orden', default=0)
    created= models.DateTimeField(verbose_name='Fecha de Creación', auto_now_add=True)
    updated= models.DateTimeField(verbose_name='Fecha de Edición', auto_now=True)

    class Meta:
        verbose_name = 'página'
        verbose_name_plural = 'páginas'
        ordering = ['order','title']
    
    def __str__(self):
        return self.title
