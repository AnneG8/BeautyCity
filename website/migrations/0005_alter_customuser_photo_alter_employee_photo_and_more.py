# Generated by Django 4.2.7 on 2024-01-28 20:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_customuser_photo_alter_employee_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='avatars/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['svg', 'jpeg', 'jpg', 'png'])], verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='employees/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['svg', 'jpeg', 'jpg', 'png'])], verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='salon',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='salons/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['svg', 'jpeg', 'jpg', 'png'])], verbose_name='изображение'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='services/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['svg', 'jpeg', 'jpg', 'png'])], verbose_name='изображение'),
        ),
    ]