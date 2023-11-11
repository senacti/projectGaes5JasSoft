# Generated by Django 4.2.6 on 2023-11-11 02:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('production', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('stock', models.IntegerField(verbose_name='Cantidad')),
                ('fabricationDate', models.DateTimeField(verbose_name='Fecha de fabricacion')),
                ('size', models.CharField(max_length=12, verbose_name='Tamaño')),
                ('color', models.CharField(max_length=20, verbose_name='Color')),
                ('state', models.CharField(max_length=12, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'producto',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Flow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FlowType', models.CharField(max_length=15, verbose_name='Tipo de flujo')),
                ('DateFlow', models.DateTimeField(default=datetime.datetime.now, verbose_name='Fecha de flujo')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product')),
                ('supplies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.supplies')),
            ],
            options={
                'verbose_name': 'Flujo',
                'verbose_name_plural': 'Flujos',
                'db_table': 'flujo',
                'ordering': ['id'],
            },
        ),
    ]
