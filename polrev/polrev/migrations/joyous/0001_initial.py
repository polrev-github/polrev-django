# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-09 02:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import ls.joyous.fields
import wagtail.contrib.routable_page.models
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailimages', '0019_delete_filter'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.routable_page.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='CancellationPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('except_date', models.DateField(help_text='For this date', verbose_name='For Date')),
                ('cancellation_title', models.CharField(blank=True, help_text='Show in place of cancelled event (Leave empty to show nothing)', max_length=255, verbose_name='Title')),
                ('cancellation_details', wagtail.core.fields.RichTextField(blank=True, help_text='Why was the event cancelled?', verbose_name='Details')),
            ],
            options={
                'verbose_name': 'Cancellation',
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=4, unique=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name_plural': 'Event Categories',
                'verbose_name': 'Event Category',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ExtraInfoPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('except_date', models.DateField(help_text='For this date', verbose_name='For Date')),
                ('extra_information', wagtail.core.fields.RichTextField(help_text='Information just for this date')),
            ],
            options={
                'verbose_name': 'Extra Event Information',
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='GroupPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('content', wagtail.core.fields.RichTextField(blank=True, default='')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='MultidayEventPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('time_from', models.TimeField(blank=True, null=True, verbose_name='Start time')),
                ('time_to', models.TimeField(blank=True, null=True, verbose_name='End time')),
                ('location', models.CharField(blank=True, max_length=255)),
                ('details', wagtail.core.fields.RichTextField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('date_from', models.DateField(default=datetime.date.today, verbose_name='Start date')),
                ('date_to', models.DateField(default=datetime.date.today, verbose_name='End date')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='joyous.EventCategory', verbose_name='Category')),
                ('group_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='multidayeventpage_events', related_query_name='multidayeventpage_event', to='joyous.GroupPage')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'verbose_name': 'Multiday Event Page',
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='RecurringEventPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('time_from', models.TimeField(blank=True, null=True, verbose_name='Start time')),
                ('time_to', models.TimeField(blank=True, null=True, verbose_name='End time')),
                ('location', models.CharField(blank=True, max_length=255)),
                ('details', wagtail.core.fields.RichTextField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('repeat', ls.joyous.fields.RecurrenceField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='joyous.EventCategory', verbose_name='Category')),
                ('group_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recurringeventpage_events', related_query_name='recurringeventpage_event', to='joyous.GroupPage')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'verbose_name': 'Recurring Event Page',
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='SimpleEventPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('time_from', models.TimeField(blank=True, null=True, verbose_name='Start time')),
                ('time_to', models.TimeField(blank=True, null=True, verbose_name='End time')),
                ('location', models.CharField(blank=True, max_length=255)),
                ('details', wagtail.core.fields.RichTextField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='joyous.EventCategory', verbose_name='Category')),
                ('group_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='simpleeventpage_events', related_query_name='simpleeventpage_event', to='joyous.GroupPage')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'verbose_name': 'One-Off Event Page',
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='PostponementPage',
            fields=[
                ('cancellationpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='joyous.CancellationPage')),
                ('time_from', models.TimeField(blank=True, null=True, verbose_name='Start time')),
                ('time_to', models.TimeField(blank=True, null=True, verbose_name='End time')),
                ('location', models.CharField(blank=True, max_length=255)),
                ('details', wagtail.core.fields.RichTextField(blank=True)),
                ('website', models.URLField(blank=True)),
                ('postponement_title', models.CharField(help_text='The title for the postponed event', max_length=255, verbose_name='Title')),
                ('date', models.DateField(verbose_name='Date')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='joyous.EventCategory', verbose_name='Category')),
                ('group_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='postponementpage_events', related_query_name='postponementpage_event', to='joyous.GroupPage')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'verbose_name': 'Postponement',
            },
            bases=('joyous.cancellationpage', models.Model),
        ),
        migrations.AddField(
            model_name='extrainfopage',
            name='overrides',
            field=models.ForeignKey(help_text='The recurring event that we are updating.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='joyous.RecurringEventPage'),
        ),
        migrations.AddField(
            model_name='cancellationpage',
            name='overrides',
            field=models.ForeignKey(help_text='The recurring event that we are updating.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='joyous.RecurringEventPage'),
        ),
    ]