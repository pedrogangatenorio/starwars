# Generated by Django 3.0.6 on 2020-05-30 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0007_auto_20200530_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterimage',
            name='file',
            field=models.FileField(blank=True, max_length=200, null=True, upload_to='characterImage', verbose_name='File'),
        ),
    ]