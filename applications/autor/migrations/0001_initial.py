# Generated by Django 3.1.1 on 2020-09-02 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('nacionalidad', models.CharField(max_length=20, verbose_name='Nacionalidad')),
                ('edad', models.PositiveIntegerField(default=0, verbose_name='Edad')),
            ],
            options={
                'verbose_name': 'El Autor',
                'verbose_name_plural': 'Los autores',
            },
        ),
    ]