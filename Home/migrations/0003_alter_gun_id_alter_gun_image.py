# Generated by Django 4.2.6 on 2023-10-11 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_alter_gun_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gun',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='gun',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]