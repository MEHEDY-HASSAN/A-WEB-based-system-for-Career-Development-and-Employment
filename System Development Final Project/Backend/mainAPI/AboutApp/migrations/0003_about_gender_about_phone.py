# Generated by Django 4.1.2 on 2022-12-08 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AboutApp', '0002_rename_login_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='Gender',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='Phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
