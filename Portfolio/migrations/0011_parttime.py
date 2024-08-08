# Generated by Django 5.0.7 on 2024-08-08 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0010_remove_profileinfo_sk_body1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('data', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('website', models.CharField(max_length=200)),
                ('information', models.TextField()),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='personal/')),
            ],
        ),
    ]
