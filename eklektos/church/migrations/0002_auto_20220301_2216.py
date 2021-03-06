# Generated by Django 3.2.8 on 2022-03-01 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('church', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='videos')),
                ('description', models.CharField(max_length=250)),
                ('affiliate_url', models.SlugField(blank=True, null=True)),
                ('artist_image', models.ImageField(default=True, upload_to='static/images/uploads')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='liked',
        ),
        migrations.RemoveField(
            model_name='post',
            name='update',
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=150),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.AddField(
            model_name='media',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='church.post'),
        ),
    ]
