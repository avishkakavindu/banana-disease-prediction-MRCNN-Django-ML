# Generated by Django 3.2.19 on 2023-07-12 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_alter_wateringplan_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diseasequestionnaireprediction',
            name='abnormal_fruiting',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='diseasequestionnaireprediction',
            name='leaf_color',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='diseasequestionnaireprediction',
            name='leaf_curling',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='diseasequestionnaireprediction',
            name='leaf_spots',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='diseasequestionnaireprediction',
            name='leaf_wilting',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='diseasequestionnaireprediction',
            name='presence_of_pests',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='diseasequestionnaireprediction',
            name='root_rot',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='diseasequestionnaireprediction',
            name='stem_color',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='diseasequestionnaireprediction',
            name='stunted_growth',
            field=models.CharField(max_length=100),
        ),
    ]