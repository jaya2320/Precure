# Generated by Django 3.1.4 on 2022-04-19 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pred', '0006_auto_20220418_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='post'),
        ),
        migrations.AlterField(
            model_name='replie',
            name='image',
            field=models.ImageField(null=True, upload_to='post'),
        ),
    ]
