# Generated by Django 3.2.11 on 2022-01-21 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joyous', '0017_extcancellationpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='closedfor',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='eventcategory',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]