# Generated by Django 3.0.6 on 2020-05-26 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_provider', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='background',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
    ]