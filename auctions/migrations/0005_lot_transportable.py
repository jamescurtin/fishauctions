# Generated by Django 3.1.1 on 2020-10-03 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_location_userpreferences'),
    ]

    operations = [
        migrations.AddField(
            model_name='lot',
            name='transportable',
            field=models.BooleanField(default=True),
        ),
    ]
