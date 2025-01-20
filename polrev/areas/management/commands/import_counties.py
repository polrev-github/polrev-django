# -*- coding: utf-8 -*-
import requests

from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand

from areas.models import State, County

import csv

import us


class Command(BaseCommand):
    help = "Import Counties from Census Bureau"

    SITE = Site.objects.get_current()

    CODES = list = [(k, v) for k, v in us.states.mapping("fips", "abbr").items()]

    def handle(self, *args, **options):
        for fips, abbr in self.CODES:
            if fips:
                self.import_state_counties(fips, abbr)
            # exit()

    def import_state_counties(self, state_fips, state_abbr):
        url = f"https://www2.census.gov/geo/docs/reference/codes/files/st{state_fips}_{state_abbr.lower()}_cou.txt"
        print(url)
        state_ref = State.objects.get(state_fips=state_fips)
        response = requests.get(url, headers={"User-Agent": "XY"})
        # print(response.__dict__)
        csv_bytestream = response.content.decode("utf-8")
        reader = csv.reader(csv_bytestream.splitlines(), delimiter=",")
        my_list = list(reader)
        for row in my_list:
            print(row)

            county = County(
                state_ref=state_ref,
                # state_usps=row[0],
                state_fips=row[1],
                county_fips=row[2],
                name=row[3],
                class_fips=row[4],
            )
            county.save()
