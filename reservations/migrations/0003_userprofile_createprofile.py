# Generated by Django 3.2.18 on 2023-05-11 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='createprofile',
            field=models.BooleanField(default=False),
        ),
    ]
