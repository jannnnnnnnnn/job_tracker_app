# Generated by Django 3.0.8 on 2020-09-10 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0009_auto_20200910_0814'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='postalcode',
            new_name='zipcode',
        ),
    ]