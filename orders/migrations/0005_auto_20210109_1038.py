# Generated by Django 3.0.1 on 2021-01-09 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20210109_0004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='dicount',
            new_name='discount',
        ),
    ]
