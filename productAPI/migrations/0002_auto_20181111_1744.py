# Generated by Django 2.1.2 on 2018-11-11 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='famille',
            name='designation',
            field=models.CharField(blank=True, default='', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='laboratoire',
            name='designation',
            field=models.CharField(blank=True, default='', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='designation',
            field=models.CharField(blank=True, default='', max_length=100, unique=True),
        ),
    ]