# Generated by Django 3.1.5 on 2021-03-21 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprojects', '0035_auto_20210320_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_type',
            field=models.CharField(default='Web Application', max_length=50),
        ),
    ]
