# Generated by Django 3.2.13 on 2022-05-01 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offices', '0004_auto_20220501_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='office',
            name='number',
            field=models.PositiveSmallIntegerField(default=0, help_text='Sorting priority.  Example: 0, 100, etc'),
        ),
    ]