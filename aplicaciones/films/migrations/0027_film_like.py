# Generated by Django 3.0.6 on 2020-08-25 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0026_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='r_like', to='films.Like'),
        ),
    ]
