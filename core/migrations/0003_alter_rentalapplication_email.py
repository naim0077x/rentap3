# Generated by Django 5.1.6 on 2025-02-15 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_traking_code_promoter_tracking_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentalapplication',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
