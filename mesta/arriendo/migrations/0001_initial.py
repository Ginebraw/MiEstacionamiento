# Generated by Django 3.1.2 on 2021-06-13 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arrendatario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=12)),
                ('nombreCom', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=50)),
                ('imgPerfil', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
