# Generated by Django 3.1.4 on 2021-01-22 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20210122_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profile_pic',
            field=models.ImageField(default='place.png', upload_to=''),
        ),
    ]