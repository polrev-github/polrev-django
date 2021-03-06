# Generated by Django 3.2.13 on 2022-05-06 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0004_campaignspage_year_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaignpage',
            name='potent',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='campaignpage',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Running'), (1, 'Dropped Out'), (2, 'Won Primary'), (3, 'Lost Primary'), (4, 'Won Race'), (5, 'Lost Race')], default=0),
        ),
    ]
