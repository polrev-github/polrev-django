# -*- coding: utf-8 -*-
import requests

from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand

from areas.models import State

import csv


class Command(BaseCommand):
    help = "Import states from Census Bureau"

    SITE = Site.objects.get_current()

    def handle(self, *args, **options):
        response = requests.get(
            "https://www2.census.gov/geo/docs/reference/state.txt",
            headers={"User-Agent": "XY"},
        )
        # print(response.__dict__)
        csv_bytestream = response.content.decode("utf-8")
        reader = csv.reader(csv_bytestream.splitlines(), delimiter="|")
        my_list = list(reader)
        print(my_list[0])  # Print the header
        my_list.pop(0)  # Pop the header
        for row in my_list:
            print(row)
            state = State(
                state_fips=row[0],
                state_usps=row[1],
                title=row[2],
                name=row[2],
                gnis_feature_id=row[3],
            )
            state.save()
