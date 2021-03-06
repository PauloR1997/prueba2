# Generated by Django 3.1.4 on 2021-01-27 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0002_auto_20210120_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('apellido', models.TextField()),
                ('sexo', models.CharField(max_length=150)),
                ('pais', models.CharField(max_length=150)),
                ('fecha_nacimiento', models.DateField()),
                ('publicado', models.BooleanField()),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
