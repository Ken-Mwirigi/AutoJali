# Generated by Django 4.2 on 2024-12-04 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AutoJaliApp', '0007_alter_carowners_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carowners',
            name='user',
        ),
    ]
