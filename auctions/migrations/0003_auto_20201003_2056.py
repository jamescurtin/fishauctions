# Generated by Django 3.1.1 on 2020-10-03 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auto_20201003_2046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpreferences',
            name='club',
        ),
        migrations.RemoveField(
            model_name='userpreferences',
            name='location',
        ),
        migrations.RemoveField(
            model_name='userpreferences',
            name='user',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='UserPreferences',
        ),
    ]