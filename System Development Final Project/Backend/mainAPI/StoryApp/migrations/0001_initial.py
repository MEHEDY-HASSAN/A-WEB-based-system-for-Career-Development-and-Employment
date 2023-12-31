# Generated by Django 4.1.2 on 2022-12-23 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('StoryID', models.AutoField(primary_key=True, serialize=False)),
                ('ProfileID', models.IntegerField(blank=True)),
                ('ProfileName', models.CharField(max_length=100)),
                ('ProfilePicture', models.CharField(blank=True, max_length=2000)),
                ('StoryDate', models.DateTimeField(auto_now_add=True)),
                ('StoryImage', models.CharField(blank=True, max_length=2000)),
            ],
        ),
    ]
