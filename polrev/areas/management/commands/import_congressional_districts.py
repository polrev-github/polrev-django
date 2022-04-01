# -*- coding: utf-8 -*-
import re
import uuid
from datetime import datetime
import json
from urllib.parse import urlparse
from pathlib import Path

import asyncio
from asgiref.sync import sync_to_async

import requests
from markdown import markdown

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.core.files import File
#from django.core.management.base import CommandError, LabelCommand
from django.core.management.base import BaseCommand, CommandError
from django.template.defaultfilters import slugify
from django.utils.html import strip_tags

import csv

from areas.models import State, CongressionalDistrict


#class Command(LabelCommand):
class Command(BaseCommand):
    help = 'Import states from Census Bureau'

    SITE = Site.objects.get_current()

    def handle(self, *args, **options):
        response = requests.get('https://www2.census.gov/geo/docs/reference/codes/files/national_cd113.txt', headers={"User-Agent": "XY"})
        #print(response.__dict__)
        csv_bytestream = response.content.decode('utf-8')
        my_list = csv_bytestream.splitlines()
        print(my_list[0]) # Print the header
        my_list.pop(0) # Pop the header
        for line in my_list:
            row = (line[:2], line[8:10], line[16:18], line[24:])
            print(row)
            cd_fips=row[2]
            if cd_fips == 'ZZ':
                continue
            cd_num = int(cd_fips)
            state_ref = State.objects.get(state_fips=row[1])
            
            district = CongressionalDistrict(
                state_fips=row[1],
                cd_fips=row[2],
                name=row[3],
                cd_num=cd_num,
                state_ref=state_ref,
            )
            district.save()
