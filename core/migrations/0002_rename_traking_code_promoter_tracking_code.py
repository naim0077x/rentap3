# Generated by Django 5.1.6 on 2025-02-15 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='promoter',
            old_name='traking_code',
            new_name='tracking_code',
        ),
    ]
