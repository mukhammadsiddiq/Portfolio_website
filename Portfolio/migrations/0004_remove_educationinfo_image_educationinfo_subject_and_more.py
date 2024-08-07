# Generated by Django 5.0.7 on 2024-08-07 09:41

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0003_educationinfo_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='educationinfo',
            name='image',
        ),
        migrations.AddField(
            model_name='educationinfo',
            name='subject',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='educationinfo',
            name='video',
            field=models.URLField(blank=True, null=True),
        ),
    ]
