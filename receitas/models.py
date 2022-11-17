from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Receita(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.TextField()
    categoria = models.CharField(max_length=200)
    date_receita = models.DateField(default=datetime.now, blank=True)
    publicada = models.BooleanField(default=False)
    imagem_receita = models.ImageField(upload_to='fotos/%d/%m/y', blank=True)
