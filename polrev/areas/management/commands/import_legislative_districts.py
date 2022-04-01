# -*- coding: utf-8 -*-
import re
import uuid
from datetime import datetime
import json
from urllib.parse import urlparse
from pathlib import Path

import requests
from markdown import markdown

from django.conf import settings
from django.core.files.temp import NamedTemporaryFile
#from django.core.management.base import CommandError, LabelCommand
from django.core.management.base import BaseCommand, CommandError
from django.template.defaultfilters import slugify
from django.utils.html import strip_tags
from django.core.files.images import ImageFile

from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

import csv

from areas.models import State, StateSenateDistrict, StateHouseDistrict


# fips, usps, senate districts, senate seats, house districts, house seats
DATA = [
    ('01', 'AL', 35, 35, 105, 105),
    ('02', 'AK', 20, 20, 40, 40),
    ('04', 'AZ', 30, 30, 30, 60),
    ('05', 'AR', 35, 35, 100, 100),
    ('06', 'CA', 40, 40, 80, 80),
    ('08', 'CO', 35, 35, 65, 65),
    ('09', 'CT', 36, 36, 151, 151),
    ('10', 'DE', 21, 21, 41, 41),
    #('11', 'DC', 21, 21, 41, 41),
    ('12', 'FL', 40, 40, 120, 120),
    ('13', 'GA', 56, 56, 180, 180),
    ('15', 'HI', 25, 25, 51, 51),
    ('16', 'ID', 35, 35, 35, 70),
    ('17', 'IL', 59, 59, 118, 118),
    ('18', 'IN', 50, 50, 100, 100),
    ('19', 'IA', 50, 50, 100, 100),
    ('20', 'KS', 40, 40, 125, 125),
    ('21', 'KY', 38, 38, 100, 100),
    ('22', 'LA', 39, 39, 105, 105),
    ('23', 'ME', 35, 35, 151, 151),
    ('24', 'MD', 47, 47, 67, 141),
    ('25', 'MA', 40, 40, 160, 160),
    ('26', 'MI', 38, 38, 110, 110),
    ('27', 'MN', 67, 67, 134, 134),
    ('28', 'MS', 52, 52, 122, 122),
    ('29', 'MO', 34, 34, 163, 163),
    ('30', 'MT', 50, 50, 100, 100),
    ('31', 'NE', 49, 49, 0, 0),
    ('32', 'NV', 21, 21, 42, 42),
    ('33', 'NH', 24, 24, 204, 400),
    ('34', 'NJ', 40, 40, 40, 80),
    ('35', 'NM', 42, 42, 70, 70),
    ('36', 'NY', 63, 63, 150, 150),
    ('37', 'NC', 50, 50, 120, 120),
    ('38', 'ND', 47, 47, 47, 94),
    ('39', 'OH', 33, 33, 99, 99),
    ('40', 'OK', 48, 48, 101, 101),
    ('41', 'OR', 30, 30, 60, 60),
    ('42', 'PA', 50, 50, 203, 203),
    ('44', 'RI', 38, 38, 75, 75),
    ('45', 'SC', 46, 46, 124, 124),
    ('46', 'SD', 35, 35, 37, 70),
    ('47', 'TN', 33, 33, 99, 99),
    ('48', 'TX', 31, 31, 150, 150),
    ('49', 'UT', 29, 29, 75, 75),
    ('50', 'VT', 13, 30, 104, 150),
    ('51', 'VA', 40, 40, 100, 100),
    ('53', 'WA', 49, 49, 49, 98),
    ('54', 'WV', 17, 34, 67, 100),
    ('55', 'WI', 33, 33, 99, 99),
    ('56', 'WY', 30, 30, 60, 60),
]

#class Command(LabelCommand):
class Command(BaseCommand):
    help = 'Import Legislative Districts'

    def handle(self, *args, **options):
        for state_fips, usps, sd, ss, hd, hs in DATA:
            print(state_fips, usps, sd, ss, hd, hs)
            state_ref = State.objects.get(state_fips=state_fips)

            for i in range(1, sd+1):
                district_u = StateSenateDistrict(
                    state_fips=state_fips,
                    district_num=i,
                    seats=ss/sd,
                    state_ref=state_ref,
                )
                district_u.save()

            for j in range(1, hd+1):
                district_l = StateHouseDistrict(
                    state_fips=state_fips,
                    district_num=j,
                    seats=hs/hd,
                    state_ref=state_ref,
                )
                district_l.save()
