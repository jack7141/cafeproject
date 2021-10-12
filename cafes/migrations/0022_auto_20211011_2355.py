# Generated by Django 3.2.6 on 2021-10-11 14:55

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('cafes', '0021_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafe',
            name='newcontinent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cafeCity', to='cafes.city'),
        ),
        migrations.AddField(
            model_name='cafe',
            name='newcountry',
            field=smart_selects.db_fields.ChainedForeignKey(blank=True, chained_field='newcontinent', chained_model_field='continent', null=True, on_delete=django.db.models.deletion.CASCADE, to='cafes.country'),
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]