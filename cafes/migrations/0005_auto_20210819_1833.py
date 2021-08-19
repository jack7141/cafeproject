# Generated by Django 3.2.6 on 2021-08-19 09:33

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('cafes', '0004_auto_20210819_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafe',
            name='cafeNumber',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
        migrations.AddField(
            model_name='cafe',
            name='website',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]