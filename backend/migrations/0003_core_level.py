# Generated by Django 4.0.4 on 2022-05-25 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_boost'),
    ]

    operations = [
        migrations.AddField(
            model_name='core',
            name='level',
            field=models.IntegerField(default=0),
        ),
    ]
