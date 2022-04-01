# -*- coding: utf-8 -*-
import re
import uuid
from datetime import datetime
import json
from urllib.parse import urlparse
from pathlib import Path

import asyncio
from asgiref.sync import sync_to_async
import bs4

import requests
from markdown import markdown

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
#from django.core.management.base import CommandError, LabelCommand
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.utils.html import strip_tags
from django.utils.text import Truncator
from django.core.files.images import ImageFile

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

from areas.models import State

import csv

#class Command(LabelCommand):
class Command(BaseCommand):
    help = 'Import states from Census Bureau'

    SITE = Site.objects.get_current()

    def handle(self, *args, **options):
        response = requests.get('https://www2.census.gov/geo/docs/reference/state.txt', headers={"User-Agent": "XY"})
        #print(response.__dict__)
        csv_bytestream = response.content.decode('utf-8')
        reader = csv.reader(csv_bytestream.splitlines(), delimiter='|')
        my_list = list(reader)
        print(my_list[0]) # Print the header
        my_list.pop(0) # Pop the header
        for row in my_list:
            print(row)
            state = State(
                state_fips=row[0],
                state_usps=row[1],
                title=row[2],
                name=row[2],
                gnis_feature_id=row[3]
            )
            state.save()
