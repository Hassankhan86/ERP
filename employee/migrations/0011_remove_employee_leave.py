# Generated by Django 3.1.4 on 2021-03-24 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0010_auto_20210324_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='leave',
        ),
    ]
