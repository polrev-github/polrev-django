# Generated by Django 3.2.13 on 2022-05-02 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('areas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StateJudicialDistrict',
            fields=[
                ('area_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='areas.area')),
                ('district_num', models.PositiveSmallIntegerField()),
                ('state_ref', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='state_judicial_districts', to='areas.state', verbose_name='State')),
            ],
            options={
                'ordering': ['district_num'],
            },
            bases=('areas.area',),
        ),
    ]
