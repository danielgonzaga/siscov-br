from django.db import models

# Create your models here.
class Estado(models.Model):
    Id = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=100)

class Municipio(models.Model):
    Id = models.AutoField(primary_key=True)
    Nome = models.CharField(max_length=100)
    IdEstado = models.ForeignKey(Estado, on_delete=models.CASCADE)

class Casos(models.Model):
    Id = models.AutoField(primary_key=True)
    DataNotificacao = models.CharField(max_length=10)
    DataInicioSintomas = models.CharField(max_length=10)
    Idade = models.IntegerField()
    Condicoes = models.CharField(max_length=100)
    EvolucaoCaso = models.CharField(max_length=100)
    ClassificacaoFinal = models.CharField(max_length=100)
    IdMunicipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    