# Generated by Django 3.2.3 on 2021-06-08 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0004_score_datecreated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='time',
            field=models.DurationField(blank=True, null=True),
        ),
    ]
