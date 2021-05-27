# Generated by Django 3.1.4 on 2021-02-03 08:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20201231_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirement',
            name='status',
            field=models.CharField(choices=[('IN PROGRESS', 'IN PROGRESS'), ('COMPLETED', 'COMPLETED'), ('VERIFIED', 'VERIFIED')], default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]