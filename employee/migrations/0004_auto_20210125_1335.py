# Generated by Django 3.1.4 on 2021-01-25 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20210122_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeeducation',
            name='endingdate',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='employeeeducation',
            name='startingdate',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='employeeexperience',
            name='endingDate',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='employeeexperience',
            name='startingDate',
            field=models.TextField(max_length=20),
        ),
    ]