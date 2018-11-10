# Generated by Django 2.1.2 on 2018-11-10 11:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Famille',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Laboratoire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(blank=True, default='', max_length=100)),
                ('reference', models.CharField(default='', max_length=100)),
                ('creation_date', models.DateField(default=datetime.date.today)),
                ('contenantCoffret', models.IntegerField(default='1', null=True)),
                ('testContenant', models.IntegerField(default='1', null=True)),
                ('cmm', models.IntegerField(default='1', null=True)),
                ('StockMiniMois', models.IntegerField(default='1', null=True)),
                ('famille', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='productAPI.Famille')),
                ('laboratoire', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='productAPI.Laboratoire')),
            ],
        ),
    ]
