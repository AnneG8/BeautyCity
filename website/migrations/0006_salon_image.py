# Generated by Django 4.2.7 on 2024-01-28 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_customuser_verification_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='salon',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='изображение'),
        ),
    ]
