# Generated by Django 4.2.6 on 2023-10-11 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Gun',
        ),
    ]