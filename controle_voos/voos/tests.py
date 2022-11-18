from django.test import TestCase

from voos.models import companhia, voo, partida, chegada

import datetime

class CompanhiaAereaTest(TestCase):
  @classmethod
  def setUpTestData(cls):
      companhia.objects.create(nome='gol',code='GO')
      companhia.objects.create(nome='latam')
  def test_companhia_id_1(self):
      companhia_1 = companhia.objects.get(nome='gol')
      self.assertEqual(companhia_1.id, 1)
  def test_companhia_id_1(self):
      companhia_2 = companhia.objects.get(nome='latam')
      self.assertEqual(companhia_2.id, 2)
  def test_companhia_codigo_1(self):
      #https://stackoverflow.com/questions/51148893/object-created-even-if-field-was-required
      companhia_2 = companhia.objects.get(nome='latam')
      self.assertEqual(companhia_2.code, '')
  def test_update_codigo(self):
      companhia_1 = companhia.objects.get(nome='gol')
      companhia_1.code = 'GL'
      companhia_1.save()
      self.assertEqual(companhia_1.code, 'GL')

class VooModelTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    companhia.objects.create(nome='gol')
    companhia_1 = companhia.objects.get(nome='gol')
    horario = datetime.time(10,30) #10 horas e 30 min
    voo.objects.create(companhia=companhia_1, horario_previsto=horario, local='GRU', code='AAA111')

  def test_voo_codigo(self):
    companhia_1 = companhia.objects.get(nome='gol')
    voo_1 = voo.objects.get(companhia=companhia_1)
    self.assertEqual(voo_1.code, 'AAA111')

  def test_voo_id(self):
    companhia_1 = companhia.objects.get(nome='gol')
    voo_1 = voo.objects.get(companhia=companhia_1)
    self.assertEqual(voo_1.id, 1)

  def test_horario_previsto(self):
    companhia_1 = companhia.objects.get(nome='gol')
    voo_1 = voo.objects.get(companhia=companhia_1)
    self.assertEqual(voo_1.horario_previsto, datetime.time(10,30))

  def test_local(self):
    companhia_1 = companhia.objects.get(nome='gol')
    voo_1 = voo.objects.get(companhia=companhia_1)
    self.assertEqual(voo_1.local, 'GRU')

class PartidaModelTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    companhia.objects.create(nome='gol')
    companhia_1 = companhia.objects.get(nome='gol')
    horario = datetime.time(10,30) #10 horas e 30 min
    voo.objects.create(companhia=companhia_1, horario_previsto=horario, local='GRU')
    voo_1 = voo.objects.get(companhia=companhia_1)
    dia = datetime.datetime(2022, 10, 20, tzinfo=datetime.timezone.utc)
    partida.objects.create(voo=voo_1, data=dia)

  def test_partida_id(self):
    voo_1 = voo.objects.get(id=1)
    partida_1 = partida.objects.get(voo=voo_1)
    self.assertEqual(partida_1.id, 1)

  def test_partida_data(self):
    voo_1 = voo.objects.get(id=1)
    partida_1 = partida.objects.get(voo=voo_1)
    self.assertEqual(partida_1.data, datetime.datetime(2022, 10, 20, tzinfo=datetime.timezone.utc))

  def test_partida_status(self):
    voo_1 = voo.objects.get(id=1)
    partida_1 = partida.objects.get(voo=voo_1)
    self.assertEqual(partida_1.status, 'EM')

  def test_partida_horario_real(self):
    voo_1 = voo.objects.get(id=1)
    partida_1 = partida.objects.get(voo=voo_1)
    self.assertEqual(partida_1.real, None)
  
class ChegadaModelTest(TestCase):
  @classmethod
  def setUpTestData(cls):
    companhia.objects.create(nome='latam')
    companhia_1 = companhia.objects.get(nome='latam')
    horario = datetime.time(10,30) #10 horas e 30 min
    voo.objects.create(companhia=companhia_1, horario_previsto=horario, local='GRU')
    voo_1 = voo.objects.get(companhia=companhia_1)
    dia = datetime.datetime(2022, 11, 21, tzinfo=datetime.timezone.utc)
    chegada.objects.create(voo=voo_1, data=dia)

  def test_chegada_id(self):
    voo_1 = voo.objects.get(id=1)
    chegada_1 = chegada.objects.get(voo=voo_1)
    self.assertEqual(chegada_1.id, 1)

  def test_chegada_data(self):
    voo_1 = voo.objects.get(id=1)
    chegada_1 = chegada.objects.get(voo=voo_1)
    self.assertEqual(chegada_1.data, datetime.datetime(2022, 11, 21, tzinfo=datetime.timezone.utc))

  def test_chegada_status(self):
    voo_1 = voo.objects.get(id=1)
    chegada_1 = chegada.objects.get(voo=voo_1)
    self.assertEqual(chegada_1.status, 'VO')

  def test_chegada_horario_real(self):
    voo_1 = voo.objects.get(id=1)
    chegada_1 = chegada.objects.get(voo=voo_1)
    self.assertEqual(chegada_1.real, None)
  
