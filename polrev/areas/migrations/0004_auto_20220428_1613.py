# Generated by Django 3.2.13 on 2022-04-28 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offices', '0004_alter_officetype_priority'),
        ('campaigns', '0003_alter_campaignpage_date'),
        ('areas', '0003_circuitcourt_districtcourt_federalcourt_precinctcourt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='districtcourt',
            name='area_ptr',
        ),
        migrations.RemoveField(
            model_name='districtcourt',
            name='state_ref',
        ),
        migrations.RemoveField(
            model_name='federalcourt',
            name='area_ptr',
        ),
        migrations.AlterField(
            model_name='area',
            name='kind',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Unknown'), (1, 'State'), (2, 'Congressional District'), (3, 'State Senate District'), (4, 'State House District'), (5, 'County'), (6, 'City'), (7, 'Town'), (8, 'Village'), (9, 'Township'), (10, 'Charter Township'), (11, 'Borough'), (12, 'City and Borough'), (13, 'Unified Government'), (14, 'Consolidate Government'), (15, 'Metropolitan Government'), (16, 'Urban County'), (17, 'City and County'), (18, 'Municipality'), (19, 'Corporation'), (20, 'Plantation'), (23, 'Unified School District'), (24, 'Elementary School District'), (25, 'Secondary School District'), (26, 'Federal Court'), (27, 'Circuit Court'), (28, 'District Court'), (29, 'Precinct Court')], default=0),
        ),
        migrations.DeleteModel(
            name='CircuitCourt',
        ),
        migrations.DeleteModel(
            name='DistrictCourt',
        ),
        migrations.DeleteModel(
            name='FederalCourt',
        ),
    ]