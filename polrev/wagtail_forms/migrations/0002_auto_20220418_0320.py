# Generated by Django 3.2.13 on 2022-04-18 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailredirects', '0007_add_autocreate_fields'),
        ('wagtailcore', '0066_collection_management_permissions'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailsearchpromotions', '0002_capitalizeverbose'),
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formpage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='FormField',
        ),
        migrations.DeleteModel(
            name='FormPage',
        ),
    ]