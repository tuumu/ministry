# Generated by Django 3.2.8 on 2022-03-10 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_comment_chat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sermonsay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('body', models.TextField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sermon_comments', to='page.allsongs')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
