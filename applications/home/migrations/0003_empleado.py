# Generated by Django 3.1 on 2020-09-02 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200902_1129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.persona')),
                ('empleo', models.CharField(max_length=50, verbose_name='Empleo')),
            ],
            bases=('home.persona',),
        ),
    ]
