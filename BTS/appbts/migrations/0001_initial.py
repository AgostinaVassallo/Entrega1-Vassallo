# Generated by Django 4.1.3 on 2022-12-09 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Army',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resumen', models.CharField(max_length=50)),
                ('poder_economico', models.CharField(max_length=50)),
                ('influencia', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Bts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trayectoria', models.CharField(max_length=50)),
                ('integrantes', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('carrera_musical', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Corea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('historia', models.CharField(max_length=50)),
                ('industria_cultural', models.CharField(max_length=50)),
                ('soft_power', models.CharField(max_length=50)),
                ('servicio_militar', models.CharField(max_length=50)),
            ],
        ),
    ]