# Generated by Django 3.1.4 on 2021-05-26 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0003_remove_bugs_project_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugs',
            name='bug_pic',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
