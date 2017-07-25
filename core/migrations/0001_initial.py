# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-25 15:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('neighborhood', models.CharField(max_length=100, verbose_name='Bairro')),
                ('address', models.CharField(max_length=200, verbose_name='Endereço')),
                ('price', models.IntegerField(verbose_name='Cachê')),
                ('contact', models.CharField(max_length=100, verbose_name='Contato')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
            options={
                'verbose_name': 'Artista',
                'verbose_name_plural': 'Artistas',
                'ordering': ['state', 'city', 'neighborhood', 'name'],
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Cidade')),
            ],
            options={
                'verbose_name': 'Cidade',
                'verbose_name_plural': 'Cidades',
                'ordering': ['state', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('owner', models.CharField(max_length=100, verbose_name='Responsável')),
                ('opened', models.CharField(max_length=100, verbose_name='Horário de funcionamento')),
                ('neighborhood', models.CharField(max_length=100, verbose_name='Bairro')),
                ('address', models.CharField(max_length=200, verbose_name='Endereço')),
                ('contact', models.CharField(max_length=100, verbose_name='Contato')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.City', verbose_name='Cidade')),
            ],
            options={
                'verbose_name': 'Espaço',
                'verbose_name_plural': 'Espaços',
                'ordering': ['state', 'city', 'name'],
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gener', models.CharField(max_length=100, verbose_name='Gênero')),
            ],
            options={
                'verbose_name': 'Gênero',
                'verbose_name_plural': 'Gêneros',
                'ordering': ['gener'],
            },
        ),
        migrations.AddField(
            model_name='club',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.State', verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.State', verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='artist',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.City', verbose_name='Cidade'),
        ),
        migrations.AddField(
            model_name='artist',
            name='gener',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Style', verbose_name='Gênero'),
        ),
        migrations.AddField(
            model_name='artist',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.State', verbose_name='Estado'),
        ),
    ]
