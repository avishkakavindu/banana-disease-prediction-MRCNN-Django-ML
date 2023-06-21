# Generated by Django 3.2.19 on 2023-06-21 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fertilizerplan',
            name='fertilizer_type',
            field=models.CharField(choices=[('Organic Fertilizer', 'Organic Fertilizer'), ('Inorganic Fertilizer', 'Inorganic Fertilizer'), ('Slow-Release Fertilizer', 'Slow-Release Fertilizer'), ('Liquid Fertilizer', 'Liquid Fertilizer'), ('Balanced Fertilizer', 'Balanced Fertilizer'), ('Controlled-Release Fertilizer', 'Controlled-Release Fertilizer')], max_length=200),
        ),
    ]
