# Generated by Django 4.2.5 on 2023-11-03 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicacion',
            name='categorias',
        ),
        migrations.RemoveField(
            model_name='publicacion',
            name='fecha_publicacion',
        ),
        migrations.AddField(
            model_name='publicacion',
            name='contenido',
            field=models.TextField(default='Sin contenido'),
        ),
    ]
