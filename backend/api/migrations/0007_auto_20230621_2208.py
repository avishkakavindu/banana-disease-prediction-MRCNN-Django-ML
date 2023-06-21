# Generated by Django 3.2.19 on 2023-06-21 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20230621_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fertilizerplan',
            name='variety',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.variety'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='wateringplan',
            name='variety',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.variety'),
        ),
    ]
