# Generated by Django 3.1.1 on 2020-09-02 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Categoria del libro',
                'verbose_name_plural': 'Categoria de libros',
            },
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Titulo')),
                ('fecha', models.DateField(verbose_name='Fecha de lanzamiento')),
                ('portada', models.ImageField(upload_to='libro')),
                ('visitas', models.PositiveIntegerField(verbose_name='Visitas')),
                ('autores', models.ManyToManyField(to='autor.Autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria_libro', to='libro.categoria')),
            ],
            options={
                'verbose_name': 'El Libro',
                'verbose_name_plural': 'Los Libros',
                'ordering': ['titulo', 'fecha'],
            },
        ),
    ]
