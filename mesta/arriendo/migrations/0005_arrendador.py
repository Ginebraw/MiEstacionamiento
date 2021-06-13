# Generated by Django 3.1.2 on 2021-06-13 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arriendo', '0004_auto_20210613_0030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arrendador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=12)),
                ('nom', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=50)),
                ('imgPerfil', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]