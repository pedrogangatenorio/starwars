# Generated by Django 3.0.6 on 2020-05-31 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0017_auto_20200531_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='character',
            field=models.ManyToManyField(blank=True, help_text='Select a character for this film', to='films.Character'),
        ),
    ]