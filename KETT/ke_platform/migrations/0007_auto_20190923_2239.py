# Generated by Django 2.2.5 on 2019-09-23 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ke_platform', '0006_auto_20190923_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='orders',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]
