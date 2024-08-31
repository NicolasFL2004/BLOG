from django.db import models

# Create your models here.
class Jogos(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='jogos', null=True, blank=True)
    descricao = models.TextField()
    
    def __str__(self):
        return self.nome

class Animes(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='animes', null=True, blank=True)
    descricao = models.TextField()
    
    def __str__(self):
        return self.nome
    