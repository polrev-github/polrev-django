# Generated by Django 3.2.12 on 2022-02-14 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('states', '0001_initial'),
        ('candidates', '0003_candidatepage_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatepage',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='candidates', to='states.statepage'),
        ),
    ]