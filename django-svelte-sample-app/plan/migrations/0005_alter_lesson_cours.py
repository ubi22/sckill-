# Generated by Django 5.0.2 on 2024-02-16 18:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0004_trainingcours_students_alter_trainingcours_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='cours',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='plan.trainingcours'),
        ),
    ]
