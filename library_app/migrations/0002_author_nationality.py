# Generated by Django 5.0.7 on 2024-11-18 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='nationality',
            field=models.CharField(default='Unknown', max_length=100),
        ),
    ]
