import uuid
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from stdimage.models import StdImageField

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Categoria(models.Model):
    categoria = models.CharField('Categoria', max_length=100)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.categoria

class Cargo(models.Model):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
    
    def __str__(self):
        return self.cargo

class Post(models.Model):
    titulo = models.CharField('Titulo', max_length=100)
    categoria = models.ForeignKey('app.Categoria',verbose_name='Categoria', on_delete=models.CASCADE)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 1024, 'height': 768, 'crop': True }})
    intro = models.TextField('Introdução', max_length=250)
    conteudo = models.TextField('Conteudo')
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    cargo = models.ForeignKey('app.Cargo',verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.TextField('Bio', max_length=300)
    foto = StdImageField('Foto', upload_to=get_file_path, variations={'thumb': {'width': 600, 'height': 600, 'crop': True }})
    linkedin = models.CharField('Linkedin', max_length=100, default='#')
    facebook = models.CharField('Facebook', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')
    criado = models.DateTimeField('Criação',auto_now_add=True)

    class Meta:
        ordering = ['-criado',]

    def __str__(self):
        return self.titulo + ' | ' + str(self.autor)





