# Generated by Django 3.2.19 on 2023-06-19 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_auto_20230618_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fertilizerplanprediction',
            name='description',
        ),
    ]
