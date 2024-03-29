# Generated by Django 5.0.2 on 2024-02-16 15:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0003_alter_trainingcours_owner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingcours',
            name='students',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='trainingcours',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='training_courses', to=settings.AUTH_USER_MODEL),
        ),
    ]
