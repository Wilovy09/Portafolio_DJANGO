# Generated by Django 4.2.7 on 2023-11-07 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0002_alter_proyecto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='imagen',
            field=models.ImageField(upload_to='proyectos/images'),
        ),
    ]
