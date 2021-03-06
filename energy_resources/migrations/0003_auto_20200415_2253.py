# Generated by Django 3.0.5 on 2020-04-15 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy_resources', '0002_energyresource_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='energyresource',
            name='consumption',
            field=models.FloatField(default=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='energyresource',
            name='net_energy',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
