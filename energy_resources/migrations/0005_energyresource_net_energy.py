# Generated by Django 3.0.5 on 2020-04-21 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy_resources', '0004_remove_energyresource_net_energy'),
    ]

    operations = [
        migrations.AddField(
            model_name='energyresource',
            name='net_energy',
            field=models.FloatField(default=0),
        ),
    ]