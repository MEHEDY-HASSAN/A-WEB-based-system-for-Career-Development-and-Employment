# Generated by Django 4.1.2 on 2022-12-08 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('ProfileID', models.IntegerField(primary_key=True, serialize=False)),
                ('Profession', models.CharField(max_length=2000)),
                ('Location', models.CharField(max_length=2000)),
                ('skill', models.CharField(max_length=3000)),
            ],
        ),
    ]
