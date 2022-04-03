# Generated by Django 4.0.3 on 2022-03-05 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0002_auto_20220301_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videos', models.FileField(upload_to='videos')),
                ('descriptions', models.CharField(max_length=250)),
                ('affiliate_urls', models.SlugField(blank=True, null=True)),
                ('artist_images', models.ImageField(default=True, upload_to='static/images/uploads')),
            ],
        ),
    ]
