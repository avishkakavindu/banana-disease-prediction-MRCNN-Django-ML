# Generated by Django 3.2.19 on 2023-06-21 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20230621_2200'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='fertilizerplan',
            unique_together={('stage', 'variety')},
        ),
        migrations.AlterUniqueTogether(
            name='wateringplan',
            unique_together={('stage', 'variety')},
        ),
    ]
