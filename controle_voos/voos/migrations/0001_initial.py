# Generated by Django 4.1.3 on 2022-11-25 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='companhia',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'companhia',
            },
        ),
        migrations.CreateModel(
            name='Voo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('code', models.CharField(default='AAA111', max_length=6)),
                ('horario_previsto', models.TimeField()),
                ('local', models.CharField(max_length=200)),
                ('data', models.DateField(blank=True, null=True, verbose_name='Date')),
                ('companhia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voos.companhia')),
            ],
            options={
                'db_table': 'voo',
            },
        ),
        migrations.CreateModel(
            name='partida',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('real', models.TimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('EMb', 'Embarcando'), ('CAN', 'Cancelado'), ('PRG', 'Programado'), ('TAX', 'Taxeando'), ('PRO', 'Pronto'), ('AUT', 'Autorizado'), ('VOO', 'Em voo')], default='EM', max_length=3)),
                ('data', models.DateField(null=True)),
                ('voo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voos.voo')),
            ],
            options={
                'db_table': 'partida',
            },
        ),
        migrations.CreateModel(
            name='chegada',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('real', models.TimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('VO0', 'Em voo'), ('ATR', 'Aterrisado')], default='VO', max_length=3)),
                ('data', models.DateField()),
                ('voo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voos.voo')),
            ],
            options={
                'db_table': 'chegada',
            },
        ),
    ]
