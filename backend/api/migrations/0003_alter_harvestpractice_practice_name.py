# Generated by Django 3.2.19 on 2023-06-21 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_fertilizerplan_fertilizer_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='harvestpractice',
            name='practice_name',
            field=models.CharField(max_length=100),
        ),
    ]