# Generated by Django 4.1.2 on 2022-12-25 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WorkApp', '0003_catagory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catagory',
            old_name='catSub',
            new_name='CatSub',
        ),
    ]
