# Generated by Django 5.0.7 on 2024-08-08 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0013_parttime_addres1_parttime_addres2_parttime_body1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parttime',
            name='addres1',
        ),
        migrations.RemoveField(
            model_name='parttime',
            name='addres2',
        ),
        migrations.RemoveField(
            model_name='parttime',
            name='body1',
        ),
        migrations.RemoveField(
            model_name='parttime',
            name='body2',
        ),
        migrations.RemoveField(
            model_name='parttime',
            name='company1',
        ),
        migrations.RemoveField(
            model_name='parttime',
            name='company2',
        ),
        migrations.RemoveField(
            model_name='parttime',
            name='data1',
        ),
        migrations.RemoveField(
            model_name='parttime',
            name='data2',
        ),
        migrations.RemoveField(
            model_name='parttime',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='parttime',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='parttime',
            name='information1',
        ),
        migrations.RemoveField(
            model_name='parttime',
            name='information2',
        ),
        migrations.RemoveField(
            model_name='parttime',
            name='title1',
        ),
        migrations.RemoveField(
            model_name='parttime',
            name='title2',
        ),
        migrations.RemoveField(
            model_name='parttime',
            name='website1',
        ),
        migrations.RemoveField(
            model_name='parttime',
            name='website2',
        ),
    ]