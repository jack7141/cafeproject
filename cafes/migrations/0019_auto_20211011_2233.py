# Generated by Django 3.2.6 on 2021-10-11 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafes', '0018_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='continent',
        ),
        migrations.AddField(
            model_name='country',
            name='continent',
            field=models.ManyToManyField(blank=True, related_name='cafeCity', to='cafes.City'),
        ),
    ]
