# Generated by Django 3.0.6 on 2020-08-13 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('films', '0018_film_character'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntuacion', models.PositiveIntegerField()),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='films.Film', verbose_name='Film')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Score',
                'verbose_name_plural': 'Scores',
            },
        ),
    ]
