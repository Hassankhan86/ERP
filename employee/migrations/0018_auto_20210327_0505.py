# Generated by Django 3.1.4 on 2021-03-27 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0017_auto_20210327_0435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeesalarycalculations',
            name='leaves',
            field=models.TextField(blank=True, default=None, max_length=50),
        ),
    ]