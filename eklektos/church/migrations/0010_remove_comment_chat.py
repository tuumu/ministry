# Generated by Django 4.0.3 on 2022-03-25 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0009_comment_pics_day_sermonsay_whatusay_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='chat',
        ),
    ]
