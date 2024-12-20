# Generated by Django 5.1.3 on 2024-12-10 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelo',
            name='codigo',
        ),
        migrations.RemoveField(
            model_name='modelo',
            name='description',
        ),
        migrations.AddField(
            model_name='modelo',
            name='Collaborators',
            field=models.CharField(default='', max_length=40, verbose_name='Collaborator'),
        ),
        migrations.AddField(
            model_name='modelo',
            name='capacity',
            field=models.CharField(default='', max_length=30, verbose_name='Capacity Scale'),
        ),
        migrations.AddField(
            model_name='modelo',
            name='client',
            field=models.CharField(default='', max_length=40, verbose_name='Client Name'),
        ),
        migrations.AddField(
            model_name='modelo',
            name='idclient',
            field=models.CharField(default='', max_length=10, unique=True, verbose_name='id'),
        ),
        migrations.AddField(
            model_name='modelo',
            name='typescale',
            field=models.CharField(default='', max_length=20, verbose_name='Scale Model'),
        ),
    ]
