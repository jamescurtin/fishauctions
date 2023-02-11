# Generated by Django 4.0.3 on 2023-02-11 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0108_auction_allow_bidding_on_lots_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctiontos',
            name='memo',
            field=models.CharField(blank=True, help_text='Only other auction admins can see this', max_length=500, null=True),
        ),
    ]