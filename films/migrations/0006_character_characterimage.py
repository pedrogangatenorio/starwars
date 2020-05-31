# Generated by Django 3.0.6 on 2020-05-30 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0005_film'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('file', models.FileField(blank=True, max_length=200, null=True, upload_to='films/static/images', verbose_name='File')),
            ],
            options={
                'verbose_name': 'File',
                'verbose_name_plural': 'Files',
            },
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('height', models.CharField(max_length=100)),
                ('mass', models.CharField(max_length=100)),
                ('hair_color', models.CharField(max_length=100)),
                ('skin_color', models.CharField(max_length=100)),
                ('eye_color', models.CharField(max_length=100)),
                ('birth_year', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('homeworld', models.CharField(max_length=100)),
                ('films', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=100)),
                ('starships', models.CharField(max_length=100)),
                ('created', models.CharField(max_length=100)),
                ('edited', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('autorizado', models.ManyToManyField(blank=True, null=True, related_name='r_imagen', to='films.CharacterImage', verbose_name='Imagen')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]