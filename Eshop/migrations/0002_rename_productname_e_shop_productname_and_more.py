# Generated by Django 4.0.4 on 2022-08-21 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Eshop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='e_shop',
            old_name='productname',
            new_name='Productname',
        ),
        migrations.RenameField(
            model_name='e_shop',
            old_name='Description',
            new_name='Quantity',
        ),
    ]
