# Generated by Django 5.0.2 on 2024-02-16 14:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='cours',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='plan.trainingcours'),
            preserve_default=False,
        ),
    ]