# Generated by Django 3.1.4 on 2021-03-29 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0019_employee_joiningdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='joiningdate',
            field=models.DateTimeField(blank=True, default=None, max_length=20),
        ),
    ]
