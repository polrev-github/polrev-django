# -*- coding: utf-8 -*-
from doctest import SKIP
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

from areas.models import Area, State, County, Place

import csv

import us

import chardet
import unicodedata

#class Command(LabelCommand):
class Command(BaseCommand):
    help = 'Import Counties from Census Bureau'

    SITE = Site.objects.get_current()

    CODES = list = [(k, v) for k, v in us.states.mapping('fips', 'abbr').items()]

    SKIP_STATE = ['AS', 'GU', 'MP', 'PR', 'VI']
    SKIP_TYPE = ['CDP']
    SKIP_STAT = ['F', 'N', 'S']

    KIND_MAP = {
        'city': Area.KIND_CITY,
        'town': Area.KIND_TOWN,
        'village': Area.KIND_VILLAGE,
        'township': Area.KIND_TOWNSHIP,
        'charter_township': Area.KIND_CHARTER_TOWNSHIP,
        'borough': Area.KIND_BOROUGH,
        'city_borough': Area.KIND_CITY_BOROUGH,
        'unified_govt': Area.KIND_UNIFIED_GOVT,
        'consolidated_govt': Area.KIND_CONSOLIDATED_GOVT,
        'metro_govt': Area.KIND_METRO_GOVT,
        'urban_county': Area.KIND_URBAN_COUNTY,
        'city_county': Area.KIND_CITY_COUNTY,
        'municipality': Area.KIND_MUNICIPALITY,
        'corporation': Area.KIND_CORPORATION,
        'plantation': Area.KIND_PLANTATION,
    }

    def handle(self, *args, **options):
        for fips, abbr in self.CODES:
            if fips:
                if not abbr in self.SKIP_STATE:
                    self.import_state_places(fips, abbr)
            #exit()

    def import_state_places(self, state_fips, state_abbr):
        url = f"https://www2.census.gov/geo/docs/reference/codes/files/st{state_fips}_{state_abbr.lower()}_places.txt"
        print(url)
        state_ref = State.objects.get(state_fips=state_fips)
        response = requests.get(url, headers={"User-Agent": "XY"})
        #print(response.__dict__)
        code_data = chardet.detect(response.content)
        print(code_data)
        encoding = code_data['encoding']
        use_remove_diacritic = encoding == 'ISO-8859-1'
        #exit()
        csv_bytestream = response.content.decode(encoding)
        reader = csv.reader(csv_bytestream.splitlines(), delimiter='|')
        my_list = list(reader)
        for row in my_list:
            if not row:
                continue #rows are seperated by newlines.  wow.

            func_stat = row[5]
            if state_abbr != 'DC' and func_stat in self.SKIP_STAT:
                continue

            place_fips = row[2]
            if place_fips == '00000':
                continue

            place_name = row[3]
            place_name_parts = place_name.split()

            if place_name_parts[-1] == '(balance)': #wtf
                place_name_parts.pop()

            place_type = place_name_parts.pop()

            if place_type in self.SKIP_TYPE:
                continue

            print(row)

            kind = Area.KIND_UNKNOWN

            if place_type == 'township':
                if place_name_parts[-1] == 'charter':
                    place_name_parts.pop()
                    place_name_parts.append('Charter Township')
                    place_type = 'charter_township'
                else:
                    place_name_parts.append('Township')

            elif place_type == 'borough':
                if place_name_parts[-1] == 'and':
                    place_name_parts.pop() # pop 'and'
                    place_name_parts.pop() # pop 'city'
                    place_type = 'city_borough'

            elif place_type == 'government':
                if place_name_parts[-1] == 'unified':
                    place_name_parts.pop()
                    place_type = 'unified_govt'
                elif place_name_parts[-1] == 'consolidated':
                    place_name_parts.pop()
                    place_type = 'consolidated_govt'
                elif place_name_parts[-1] == 'metro':
                    place_name_parts.pop()
                    place_type = 'metro_govt'
                elif place_name_parts[-1] == 'metropolitan':
                    place_name_parts.pop()
                    place_type = 'metro_govt'
                else:
                    raise Exception(place_type)

            elif place_type == 'county':
                if place_name_parts[-1] == 'urban':
                    place_name_parts.pop()
                    place_type = 'urban_county'
                else:
                    raise Exception(place_type)

            elif place_type == 'County':
                place_name_parts.append(place_type)
                place_type = 'city_county'

            elif place_type == 'City':
                place_name_parts.append(place_type)
                place_type = 'city'

            place_name = ' '.join(place_name_parts)
            print(place_name)
            print(place_type)
            counties = row[6].split(', ')
            print(counties)

            kind = self.KIND_MAP[place_type]
            print(kind)

            if use_remove_diacritic:
                place_name = unicodedata.normalize('NFKD', place_name).encode('ASCII', 'ignore').decode()

            place = Place(
                kind=kind,
                state_ref=state_ref,
                state_fips=state_ref.state_fips,
                place_fips=place_fips,
                name=place_name,
            )

            place.save()

            for name in counties:
                if use_remove_diacritic:
                    name = unicodedata.normalize('NFKD', name).encode('ASCII', 'ignore').decode()

                county = County.objects.get(state_ref=state_ref, name=name)
                place.counties.add(county)
