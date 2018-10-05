# Generated by Django 2.1.2 on 2018-10-05 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productAPI', '0002_auto_20181003_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='familles',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='productAPI.Famille'),
        ),
        migrations.AlterField(
            model_name='product',
            name='laboratoires',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='productAPI.Laboratoire'),
        ),
    ]
