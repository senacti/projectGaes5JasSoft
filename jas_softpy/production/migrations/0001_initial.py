# Generated by Django 4.2.6 on 2024-02-12 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('stock', models.PositiveSmallIntegerField(verbose_name='Cantidad')),
                ('size', models.CharField(max_length=12, verbose_name='Tamaño')),
                ('color', models.CharField(max_length=20, verbose_name='Color')),
                ('supplieCode', models.IntegerField(blank=True, editable=False, null=True, verbose_name='Código')),
            ],
            options={
                'verbose_name': 'Insumo',
                'verbose_name_plural': 'Insumos',
                'db_table': 'insumo',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ProductionOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Production_OrderDate', models.DateTimeField(auto_now_add=True, verbose_name='Fecha pedido produccion')),
                ('quantity_used', models.PositiveIntegerField(verbose_name='Cantidad utilizada')),
                ('supplies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.supplies', verbose_name='Insumos')),
            ],
            options={
                'verbose_name': 'Orden producción',
                'verbose_name_plural': 'ordenesproducciones',
                'db_table': 'ordenproduccion',
                'ordering': ['id'],
            },
        ),
    ]
