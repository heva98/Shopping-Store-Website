# Generated by Django 4.0.6 on 2022-08-07 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bridalsite', '0002_rename_models_product_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
