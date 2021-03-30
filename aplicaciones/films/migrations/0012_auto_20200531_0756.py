# Generated by Django 3.0.6 on 2020-05-31 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0011_auto_20200530_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='imagen',
            field=models.ManyToManyField(blank=True, help_text='Select an image for this character', to='films.CharacterImage', verbose_name='Imagen'),
        ),
    ]