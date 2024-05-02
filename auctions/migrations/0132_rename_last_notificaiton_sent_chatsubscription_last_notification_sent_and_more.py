# Generated by Django 5.0.3 on 2024-05-01 23:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0131_alter_auction_buy_now_alter_auction_reserve_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatsubscription',
            old_name='last_notificaiton_sent',
            new_name='last_notification_sent',
        ),
        migrations.AlterField(
            model_name='lot',
            name='auction',
            field=models.ForeignKey(blank=True, help_text="<span class='text-warning' id='last-auction-special'></span>Only auctions that you have <span class='text-warning'>joined</span> will be shown here. This lot must be brought to that auction", null=True, on_delete=django.db.models.deletion.SET_NULL, to='auctions.auction'),
        ),
        migrations.AlterField(
            model_name='lot',
            name='custom_lot_number',
            field=models.CharField(blank=True, help_text='You can override the default lot number with this', max_length=9, null=True, verbose_name='Lot number'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='email_me_about_new_chat_replies',
            field=models.BooleanField(blank=True, default=True, help_text="When you comment on lots you don't own, send any new messages about that lot to your email"),
        ),
    ]
