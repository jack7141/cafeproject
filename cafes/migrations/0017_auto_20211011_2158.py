# Generated by Django 3.2.6 on 2021-10-11 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafes', '0016_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='created',
        ),
        migrations.RemoveField(
            model_name='city',
            name='updated',
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
