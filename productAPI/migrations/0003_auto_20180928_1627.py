# Generated by Django 2.0.2 on 2018-09-28 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productAPI', '0002_auto_20180928_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='reference',
            field=models.CharField(default='', max_length=100),
        ),
    ]
