# Generated by Django 3.1.5 on 2021-01-15 19:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myprojects', '0008_auto_20210115_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectupdate',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]