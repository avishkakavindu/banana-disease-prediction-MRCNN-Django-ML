# Generated by Django 3.2.19 on 2023-06-24 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_rename_fertilizer_plan_fertilizerplanprediction_dose'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fertilizerplanprediction',
            old_name='fertilizer_type',
            new_name='fertilizer_plan',
        ),
    ]