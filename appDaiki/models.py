from django.db import models

# Create your models here.

class Carreira(models.Model):
  title = models.CharField(max_length=50)
  titulos = models.CharField(max_length=20)
  ano_criacao = models.DateField()
  idade = models.CharField(max_length=20)

class Estats(models.Model):
  OPTIONS = [
    ('10', 'Top 10'),
    ('5', 'Top 5'),
    ('20', 'Top 20'),
  ]
  CATEGORY = [
    ('J', 'Estatisticas de jogo'),
    ('C', 'Estatisticas de carreira'),
  ]
  title = models.CharField(max_length=50)
  podium = models.CharField(max_length=2, choices=OPTIONS)
  priority = models.IntegerField()
  category = models.CharField(max_length=1, choices=CATEGORY)
  
class Premios(models.Model):
  OPCOES = [
    ('5', 'Top 5'),
    ('10', 'Top 10'), 
    ('50', 'Top 50'),
    ('1', 'Top 1')
  ]
  title = models.CharField(max_length=40)
  quantidade = models.CharField(max_length=10)
  maiorquantidade = models.IntegerField()
  podium = models.CharField(max_length=2, choices=OPCOES)