# Generated by Django 5.0.8 on 2024-09-14 00:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0147_auction_message_users_when_lots_sell_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="userdata",
            name="push_notifications_when_lots_sell",
            field=models.BooleanField(
                blank=True,
                default=False,
                help_text="For in-person auctions, get a notification when bidding starts on a lot that you've watched",
            ),
        ),
    ]
