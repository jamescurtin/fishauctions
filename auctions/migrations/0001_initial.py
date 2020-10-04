# Generated by Django 3.1.1 on 2020-09-14 00:51

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('sealed_bid', models.BooleanField(default=False)),
                ('lot_entry_fee', models.PositiveIntegerField(default=0, help_text='The amount, in dollars, that each seller will be charged for registering a lot', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('winning_bid_percent_to_club', models.PositiveIntegerField(default=0, help_text='To give 70% of the final bid to the seller, enter 30 here', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('bill_for_unsold_lots', models.BooleanField(default=False)),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('watch_warning_email_sent', models.BooleanField(default=False)),
                ('invoiced', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('sold', models.TextField(blank=True)),
                ('total_sold', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('bought', models.TextField(blank=True)),
                ('total_bought', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('paid', models.BooleanField(default=False)),
                ('email_sent', models.BooleanField(default=True)),
                ('auction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auctions.auction')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('lot_number', models.AutoField(primary_key=True, serialize=False)),
                ('lot_name', models.CharField(default='', help_text='Species name or common name', max_length=255)),
                ('image', models.ImageField(blank=True, help_text='Add a picture of the item here', upload_to='images/')),
                ('image_source', models.CharField(blank=True, choices=[('ACTUAL', 'This picture is of the exact item'), ('REPRESENTATIVE', "This is my picture, but it's not of this exact item.  e.x. This is the parents of these fry"), ('RANDOM', 'This picture is from the internet')], help_text='Where did you get this image?', max_length=20)),
                ('i_bred_this_fish', models.BooleanField(default=False, help_text='Check to get BAP points for this lot')),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('quantity', models.PositiveIntegerField(default=1, help_text='The item will not be sold unless someone bids at least this much', validators=[django.core.validators.MinValueValidator(1)])),
                ('reserve_price', models.PositiveIntegerField(default=2, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(200)])),
                ('category', models.CharField(choices=[('CICHLID_RIFT', 'Rift Lake Cichlids'), ('CICHLID_OLD', 'Old World Cichlids'), ('CICHLID_CENTRAL', 'Central American Cichlids'), ('CICHLID_SOUTH', 'South American Cichlids'), ('CATFISH_CORY', 'Corydoras'), ('CATFISH_PLECO', 'Plecostomus'), ('CATFISH_MISC', 'Other Catfish'), ('CHARACIN', 'Characins - Tetras, Pencilfish, Hatchetfish'), ('CYPRINID', 'Cyprinids - Barbs, Danios, Rasboras'), ('KILLI', 'Killifish'), ('GUPPY', 'Livebearers'), ('FISH_MISC', 'Misc and oddball fish'), ('GOLDFISH', 'Goldfish'), ('SHRIMP', 'Shrimp and inverts'), ('PLANTS', 'Plants'), ('HARDWARE', 'Hardware - Filters, tanks, substrate, etc.'), ('FOOD_DRY', 'Flake and pellet food'), ('FOOD_LIVE', 'Live food cultures'), ('OTHER', 'Uncategorized')], max_length=20)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('date_end', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('winning_price', models.PositiveIntegerField(blank=True, null=True)),
                ('banned', models.BooleanField(default=False)),
                ('watch_warning_email_sent', models.BooleanField(default=False)),
                ('auction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auctions.auction')),
                ('buyer_invoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='buyer_invoice', to='auctions.invoice')),
                ('seller_invoice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='seller_invoice', to='auctions.invoice')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='winner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.lot')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid_time', models.DateTimeField(auto_now_add=True)),
                ('amount', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('lot_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.lot')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]