# Generated by Django 5.0.7 on 2024-07-18 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lead',
            old_name='enail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='lead',
            old_name='modified_by',
            new_name='modified_at',
        ),
    ]
