# Generated by Django 3.0.6 on 2020-08-18 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0024_film_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]