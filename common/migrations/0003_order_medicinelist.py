# Generated by Django 3.2.12 on 2022-02-20 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20220219_2055'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='medicinelist',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]