# Generated by Django 3.2.8 on 2022-03-09 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_allsongs_notes_pics_day_quote_scripture_whatusay'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='chat',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='chat', to='page.allsongs'),
        ),
    ]
