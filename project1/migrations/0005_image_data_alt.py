# Generated by Django 3.1.2 on 2020-11-18 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0004_auto_20201118_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='image_data',
            name='alt',
            field=models.CharField(default='image', max_length=70),
        ),
    ]
