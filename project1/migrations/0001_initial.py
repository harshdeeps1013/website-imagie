# Generated by Django 3.1.2 on 2020-11-17 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='image_data',
            fields=[
                ('image_id', models.IntegerField(primary_key=True, serialize=False)),
                ('mail', models.IntegerField()),
            ],
        ),
    ]
