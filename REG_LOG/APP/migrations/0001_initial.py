# Generated by Django 5.1.6 on 2025-02-22 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.TextField()),
                ('uname', models.TextField()),
                ('psw', models.TextField()),
            ],
        ),
    ]
