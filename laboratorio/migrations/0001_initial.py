# Generated by Django 4.2.2 on 2023-06-24 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('cant_maq', models.IntegerField(verbose_name='Cantidad de maquinas')),
                ('capacidad', models.IntegerField()),
                ('ubicacion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Maquina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solapin', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=20)),
                ('inventario', models.CharField(max_length=50)),
                ('estado', models.CharField(choices=[('D', 'Disponible'), ('O', 'Ocupado'), ('R', 'Rota')], default='D', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('tipo', models.CharField(choices=[('A', 'Audio'), ('V', 'Video'), ('D', 'Documento'), ('P', 'Pdf'), ('O', 'Otro')], max_length=1)),
                ('autor', models.CharField(max_length=50)),
                ('descipcion', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('idioma', models.CharField(max_length=15)),
                ('fecha_publicacion', models.DateTimeField()),
            ],
        ),
    ]
