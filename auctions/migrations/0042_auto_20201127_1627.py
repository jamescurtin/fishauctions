# Generated by Django 3.1.1 on 2020-11-27 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0041_auto_20201124_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='pageview',
            name='blog_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.blogpost'),
        ),
        migrations.AlterField(
            model_name='pageview',
            name='lot_number',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.lot'),
        ),
    ]