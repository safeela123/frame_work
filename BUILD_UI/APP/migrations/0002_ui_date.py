# Generated by Django 5.1.6 on 2025-02-23 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ui',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
