from django.db import models

# Create your models here.
class aeroporto (models.Model) :
    nome 
    cidade 
    code 
    class Meta:
        db_table = 'aeroporto'

class CompanhiaAerea (models.Model):
    nome 
    code 
    class Meta:
        db_table = 'companhia_aerea'

class voo (models.Model):
    code
    origem 
    destino
    companhia
    class Meta:
        db_table = 'voo'

class orq (models.Model):
    status_ops = [
        ('EM', 'Embarcando'),
        ('CA', 'Cancelado'),
        ('PR', 'Embarcando'),
        ('TA', 'Taxeando'),
        ('PO', 'Pronto'),
        ('AU', 'Autorizado'),
        ('VO', 'Em voo'),
        ('AT', 'Aterrisado'),
    ]

    saida_prev
    chegada_prev
    saida_real
    chegada_real 
    status
    class Meta:
        db_table = 'orq'