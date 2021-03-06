# Generated by Django 3.0.6 on 2020-05-26 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_provider', '0002_person_background'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=30)),
                ('titleid', models.IntegerField()),
                ('message', models.TextField()),
                ('time', models.DateField()),
            ],
        ),
    ]
