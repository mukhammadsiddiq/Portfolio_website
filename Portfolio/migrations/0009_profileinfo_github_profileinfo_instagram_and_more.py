# Generated by Django 5.0.7 on 2024-08-07 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0008_jobinfo_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileinfo',
            name='github',
            field=models.CharField(default='https://github.com/mukhammadsiddiq', max_length=120),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='instagram',
            field=models.CharField(default='https://instagram.com/ibroximov_m_', max_length=120),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='linkedin',
            field=models.CharField(default='https://www.linkedin.com/in/ibroximov', max_length=120),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='sk_body1',
            field=models.CharField(default='info', max_length=120),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='sk_body2',
            field=models.CharField(default='info', max_length=120),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='sk_body3',
            field=models.CharField(default='info', max_length=120),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='sk_image1',
            field=models.ImageField(default='image', upload_to='personal/'),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='sk_image2',
            field=models.ImageField(default='image', upload_to='personal/'),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='sk_image3',
            field=models.ImageField(default='image', upload_to='personal/'),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='sk_title1',
            field=models.CharField(default='Backend Development', max_length=120),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='sk_title2',
            field=models.CharField(default='Data Analytics', max_length=120),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='sk_title3',
            field=models.CharField(default='Python Development', max_length=120),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='telegram',
            field=models.CharField(default='https://t.me/IbrokhimovMukhammad', max_length=120),
        ),
        migrations.AddField(
            model_name='profileinfo',
            name='year_experience',
            field=models.CharField(default='2+', max_length=120),
        ),
    ]
