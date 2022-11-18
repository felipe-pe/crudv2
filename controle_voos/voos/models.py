from django.db import models

class companhia(models.Model) :
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=200, null=False)
    code = models.CharField(max_length=6, null=False)

    class Meta:
        db_table = 'companhia'

class partida(models.Model) :
    opcoes = [
        ('EMB', 'Embarcando'),
        ('CAN', 'Cancelado'),
        ('PRG', 'Programado'),
        ('TAX', 'Taxeando'),
        ('PRO', 'Pronto'),
        ('AUT', 'Autorizado'),
        ('VOO', 'Em voo'),
    ]
    id = models.IntegerField(primary_key=True)
    voo = models.ForeignKey(voo, on_delete=models.CASCADE)
    aeroporto = models.CharField(max_length=3, null=False)
    real = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    status = models.CharField(max_length=3, opcoes=opcoes, default='EM')
    data = models.DateField(auto_now=False, auto_now_add=False, null=True)

    class Meta:
        db_table = 'partida'

class chegada(models.Model) :
    opcoes = [
        ('VO0', 'Em voo'),
        ('ATR', 'Aterrisado'),
    ]

    id = models.IntegerField(primary_key=True)
    voo = models.ForeignKey(voo, on_delete=models.CASCADE)
    aeroporto = models.CharField(max_length=3, null=False)
    real = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    status = models.CharField(max_length=3, opcoes=opcoes, default='VO')
    data = models.DateField(auto_now=False, auto_now_add=False, null=False)

    class Meta:
        db_table = 'chegada'

class voo(models.Model) :
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=6, blank=False, default='AAA111')
    companhia = models.ForeignKey(companhia, on_delete=models.CASCADE)
    horario_previsto = models.TimeField(auto_now=False, auto_now_add=False)
    destino = models.ForeignKey(partida, on_delete=models.CASCADE)
    origem = models.ForeignKey(chegada, on_delete=models.CASCADE)
    data = models.DateField('Date', blank=True, null=True)
    
    class Meta:
        db_table = 'voo'
