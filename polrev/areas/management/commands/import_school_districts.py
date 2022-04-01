
import requests

from django.conf import settings
from django.contrib.sites.models import Site
#from django.core.management.base import CommandError, LabelCommand
from django.core.management.base import BaseCommand, CommandError

from areas.models import Area, State, SchoolDistrict

import csv

import us

import chardet
import unicodedata

#class Command(LabelCommand):
class Command(BaseCommand):
    help = 'Import School Districts from Census Bureau'

    SITE = Site.objects.get_current()

    CODES = list = [(k, v) for k, v in us.states.mapping('fips', 'abbr').items()]

    SKIP_STATE = ['AS', 'GU', 'MP', 'PR', 'VI']

    KIND_MAP = {
        'Unified': Area.KIND_SD_UNIFIED,
        'Elementary': Area.KIND_SD_ELEMENTARY,
        'Secondary': Area.KIND_SD_SECONDARY,
    }

    skip_rows = []

    def handle(self, *args, **options):
        for fips, abbr in self.CODES:
            if fips:
                if not abbr in self.SKIP_STATE:
                    self.import_state_districts(fips, abbr)
            #exit()
        print(f"Skip count:  {len(self.skip_rows)}")
        print(self.skip_rows)

    def import_state_districts(self, state_fips, state_abbr):
        url = f"https://www2.census.gov/geo/docs/reference/codes/files/st{state_fips}_{state_abbr.lower()}_schdist.txt"
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
        reader = csv.reader(csv_bytestream.splitlines())
        my_list = list(reader)
        for row in my_list:
            if not row:
                continue #rows are seperated by newlines.  wow.
            if len(row) > 5:
                self.skip_rows.append(row)
                continue

            lea_code = row[2]
            lea_code_int = int(lea_code)
            if lea_code_int > 99900:
                self.skip_rows.append(row)
                continue

            name = row[3]
            district_type = row[4]

            print(row)

            kind = Area.KIND_UNKNOWN

            kind = self.KIND_MAP[district_type]

            print(kind)

            if use_remove_diacritic:
                name = unicodedata.normalize('NFKD', name).encode('ASCII', 'ignore').decode()

            district = SchoolDistrict(
                kind=kind,
                state_ref=state_ref,
                state_fips=state_ref.state_fips,
                lea_code=lea_code,
                name=name,
            )

            district.save()
