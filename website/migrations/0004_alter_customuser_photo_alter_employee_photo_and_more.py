# Generated by Django 4.2.7 on 2024-01-28 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_customuser_photo_alter_employee_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='avatars/', verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='employees/', verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='salon',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='salons/', verbose_name='изображение'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='services/', verbose_name='изображение'),
        ),
    ]
