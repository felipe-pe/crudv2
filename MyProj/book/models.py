from django.db import models

# Create your models here.
class aeroporto (models.Model) :
    nome = models.CharField(max_length=200, null=False)
    code =models.CharField(max_length=3, null=False)
    class Meta:
        db_table = 'aeroporto'

class CompanhiaAerea (models.Model):
    nome = models.CharField(max_length=200, null=False)
    code = models.CharField(max_length=2, null=False)
    class Meta:
        db_table = 'companhia_aerea'

class voo (models.Model):
    code = models.CharField(max_length=6, null=False)
    origem = models.CharField(max_length=3, null=False)
    destino = models.CharField(max_length=3, null=False)
    companhia = models.ForeignKey(CompanhiaAerea, on_delete=models.CASCADE)
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

    saida_prev = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    chegada_prev = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    saida_real = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    chegada_real = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    status = models.CharField(max_length=2, choices=status_ops, default='EM')
    class Meta:
        db_table = 'orq'