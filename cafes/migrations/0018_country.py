# Generated by Django 3.2.6 on 2021-10-11 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cafes', '0017_auto_20211011_2158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('continent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cafeCity', to='cafes.city')),
            ],
        ),
    ]
