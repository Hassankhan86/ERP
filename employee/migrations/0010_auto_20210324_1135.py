# Generated by Django 3.1.4 on 2021-03-24 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0009_auto_20210324_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='leave',
            field=models.TextField(blank=True, default=None),
        ),
    ]
