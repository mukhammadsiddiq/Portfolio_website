# Generated by Django 5.0.7 on 2024-08-07 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0005_remove_educationinfo_video_educationinfo_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('Upper_title', models.CharField(max_length=200)),
                ('data', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=200)),
                ('body1', models.TextField()),
                ('body2', models.TextField()),
                ('body3', models.TextField()),
                ('body4', models.TextField()),
                ('body5', models.TextField()),
                ('information', models.TextField()),
                ('image', models.ImageField(upload_to='personal/')),
            ],
        ),
    ]