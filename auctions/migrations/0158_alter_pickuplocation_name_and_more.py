# Generated by Django 5.1 on 2024-10-18 00:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0157_userlabelprefs_print_border_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pickuplocation",
            name="name",
            field=models.CharField(
                blank=True,
                default="",
                help_text="Location name shown to users.  e.x. University Mall in VT",
                max_length=70,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="userlabelprefs",
            name="preset",
            field=models.CharField(
                choices=[
                    ("sm", "Small (Avery 5160) (Not recommended)"),
                    ("lg", "Large (Avery 18262)"),
                    ("thermal_sm", 'Thermal 3"x2"'),
                    ("custom", "Custom"),
                ],
                default="lg",
                max_length=20,
                verbose_name="Label size",
            ),
        ),
    ]