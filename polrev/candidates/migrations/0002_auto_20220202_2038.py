# Generated by Django 3.2.11 on 2022-02-02 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatepage',
            name='facebook',
            field=models.URLField(blank=True, verbose_name='facebook'),
        ),
        migrations.AlterField(
            model_name='candidatepage',
            name='instagram',
            field=models.URLField(blank=True, verbose_name='instagram'),
        ),
        migrations.AlterField(
            model_name='candidatepage',
            name='twitter',
            field=models.URLField(blank=True, verbose_name='twitter'),
        ),
    ]