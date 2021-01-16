# Generated by Django 3.1 on 2021-01-15 05:26

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myprojects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('details', models.TextField()),
                ('link', models.URLField(null=True)),
                ('first_image', models.ImageField(blank=True, upload_to='update_images', verbose_name='Image 1')),
                ('second_image', models.ImageField(blank=True, upload_to='update_images', verbose_name='Image 2')),
                ('third_image', models.ImageField(blank=True, upload_to='update_images', verbose_name='Image 3')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myprojects.project')),
            ],
        ),
    ]