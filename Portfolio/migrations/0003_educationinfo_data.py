# Generated by Django 5.0.7 on 2024-08-07 07:02

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0002_educationinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationinfo',
            name='data',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
