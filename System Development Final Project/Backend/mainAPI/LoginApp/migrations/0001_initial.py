# Generated by Django 4.1.2 on 2022-10-26 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('loginID', models.AutoField(primary_key=True, serialize=False)),
                ('EmailAddress', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
            ],
        ),
    ]
