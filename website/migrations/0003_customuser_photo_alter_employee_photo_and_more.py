# Generated by Django 4.2.7 on 2024-01-28 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_salon_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='salon',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='изображение'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='изображение'),
        ),
    ]
