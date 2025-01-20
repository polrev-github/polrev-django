# -*- coding: utf-8 -*-
import requests

from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand

from areas.models import State, CongressionalDistrict


class Command(BaseCommand):
    help = "Import states from Census Bureau"

    SITE = Site.objects.get_current()

    def handle(self, *args, **options):
        response = requests.get(
            "https://www2.census.gov/geo/docs/reference/codes/files/national_cd113.txt",
            headers={"User-Agent": "XY"},
        )
        # print(response.__dict__)
        csv_bytestream = response.content.decode("utf-8")
        my_list = csv_bytestream.splitlines()
        print(my_list[0])  # Print the header
        my_list.pop(0)  # Pop the header
        for line in my_list:
            row = (line[:2], line[8:10], line[16:18], line[24:])
            print(row)
            cd_fips = row[2]
            if cd_fips == "ZZ":
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
