# Generated by Django 3.0.3 on 2020-11-16 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sendemail', '0006_videos_video_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='title',
            field=models.CharField(default='NULL', max_length=120),
        ),
    ]
