# Generated by Django 4.0.6 on 2022-08-13 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bridalsite', '0004_product2'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='FeatureProduct',
        ),
        migrations.RenameModel(
            old_name='Product2',
            new_name='LatestProduct',
        ),
    ]