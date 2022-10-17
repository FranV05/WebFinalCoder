from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatares', null = True, blank = True)

class Posts(models.Model):
    titulo = models.CharField(max_length=40)
    subtitulo = models.CharField(max_length=40)
    cuerpo = models.TextField(max_length=1000)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField(default=datetime.now)

    def __str__(self):
        return f'{self.titulo} por {self.autor.first_name} {self.autor.last_name}'