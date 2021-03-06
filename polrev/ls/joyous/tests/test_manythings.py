# ------------------------------------------------------------------------------
# Test Many Things Utilities
# ------------------------------------------------------------------------------
import sys
import datetime as dt
import pytz
from django.test import TestCase
from django.utils import translation
from ls.joyous.utils.manythings import (toOrdinal, toTheOrdinal,
                                        toDaysOffsetStr, hrJoin)

# ------------------------------------------------------------------------------
class Test(TestCase):
    def testToOrdinal(self):
        self.assertEqual(toOrdinal(-1), "last")
        self.assertEqual(toOrdinal(-2), "penultimate")
        self.assertEqual(toOrdinal(1), "first")
        self.assertEqual(toOrdinal(2), "second")
        self.assertEqual(toOrdinal(3), "third")
        self.assertEqual(toOrdinal(4), "fourth")
        self.assertEqual(toOrdinal(5), "fifth")

    def testToOrdinalNum(self):
        self.assertEqual(toOrdinal(6), "6th")
        self.assertEqual(toOrdinal(11), "11th")
        self.assertEqual(toOrdinal(12), "12th")
        self.assertEqual(toOrdinal(13), "13th")
        self.assertEqual(toOrdinal(21), "21st")
        self.assertEqual(toOrdinal(102), "102nd")
        self.assertEqual(toOrdinal(6543), "6543rd")

    def testToTheOrdinal(self):
        self.assertEqual(toTheOrdinal(-1), "The last")
        self.assertEqual(toTheOrdinal(-2, False), "the penultimate")
        self.assertEqual(toTheOrdinal(1), "The first")
        self.assertEqual(toTheOrdinal(2), "The second")
        self.assertEqual(toTheOrdinal(3), "The third")
        self.assertEqual(toTheOrdinal(4), "The fourth")
        self.assertEqual(toTheOrdinal(5), "The fifth")

    def testToTheOrdinalNum(self):
        self.assertEqual(toTheOrdinal(6), "The 6th")
        self.assertEqual(toTheOrdinal(11), "The 11th")
        self.assertEqual(toTheOrdinal(12), "The 12th")
        self.assertEqual(toTheOrdinal(13), "The 13th")
        self.assertEqual(toTheOrdinal(21), "The 21st")
        self.assertEqual(toTheOrdinal(102), "The 102nd")
        self.assertEqual(toTheOrdinal(6543), "The 6543rd")

    def testToDaysOffsetStr(self):
        self.assertEqual(toDaysOffsetStr(-3), "Three days before")
        self.assertEqual(toDaysOffsetStr(-2), "Two days before")
        self.assertEqual(toDaysOffsetStr(-1), "The day before")
        self.assertEqual(toDaysOffsetStr(0), "")
        self.assertEqual(toDaysOffsetStr(1), "The day after")
        self.assertEqual(toDaysOffsetStr(2), "Two days after")
        self.assertEqual(toDaysOffsetStr(3), "Three days after")
        self.assertEqual(toDaysOffsetStr(25), "Twenty-five days after")

    def testHumanReadableJoin(self):
        self.assertEqual(hrJoin([""]), "")
        self.assertEqual(hrJoin(["ice"]), "ice")
        self.assertEqual(hrJoin(["ice", "fire"]), "ice and fire")
        self.assertEqual(hrJoin(["wind", "ice", "fire"]),
                         "wind, ice and fire")
        self.assertEqual(hrJoin(["dog", "cat", "hen", "yak", "ant"]),
                         "dog, cat, hen, yak and ant")

# ------------------------------------------------------------------------------
class  TestFran??ais(TestCase):
    def setUp(self):
        translation.activate('fr')

    def tearDown(self):
        translation.deactivate()

    def testToOrdinal(self):
        self.assertEqual(toOrdinal(-1), "dernier")
        self.assertEqual(toOrdinal(-2), "avant-dernier")
        self.assertEqual(toOrdinal (1), "premier")
        self.assertEqual(toOrdinal (2), "deuxi??me")
        self.assertEqual(toOrdinal (3), "troisi??me")
        self.assertEqual(toOrdinal (4), "quatri??me")
        self.assertEqual(toOrdinal (5), "cinqui??me")

    def testToOrdinalNum(self):
        self.assertEqual(toOrdinal(6), "6me")
        self.assertEqual(toOrdinal(11), "11me")
        self.assertEqual(toOrdinal(12), "12me")
        self.assertEqual(toOrdinal(13), "13me")
        self.assertEqual(toOrdinal(21), "21me")
        self.assertEqual(toOrdinal(102), "102me")
        self.assertEqual(toOrdinal(6543), "6543me")

    def testToTheOrdinal(self):
        self.assertEqual(toTheOrdinal(-1), "Le dernier")
        self.assertEqual(toTheOrdinal(-2, True), "L'avant-dernier")
        self.assertEqual(toTheOrdinal(-2, False), "l'avant-dernier")
        self.assertEqual(toTheOrdinal(1), "La premier")
        self.assertEqual(toTheOrdinal(2, False), "la deuxi??me")
        self.assertEqual(toTheOrdinal(3), "Le troisi??me")
        self.assertEqual(toTheOrdinal(4), "Le quatri??me")
        self.assertEqual(toTheOrdinal(5), "Le cinqui??me")

    def testToTheOrdinalNum(self):
        self.assertEqual(toTheOrdinal(6), "La 6me")
        self.assertEqual(toTheOrdinal(11), "La 11me")
        self.assertEqual(toTheOrdinal(12), "La 12me")
        self.assertEqual(toTheOrdinal(13), "La 13me")
        self.assertEqual(toTheOrdinal(21), "La 21me")
        self.assertEqual(toTheOrdinal(102), "La 102me")
        self.assertEqual(toTheOrdinal(6543), "La 6543me")

    def testToDaysOffsetStr(self):
        self.assertEqual(toDaysOffsetStr(-3), "Trois jours avant")
        self.assertEqual(toDaysOffsetStr(-2), "Deux jours avant")
        self.assertEqual(toDaysOffsetStr(-1), "Le jour pr??c??dent")
        self.assertEqual(toDaysOffsetStr(0), "")
        self.assertEqual(toDaysOffsetStr(1), "Le jour apr??s")
        self.assertEqual(toDaysOffsetStr(2), "Deux jours apr??s")
        self.assertEqual(toDaysOffsetStr(3), "Trois jours apr??s")
        self.assertEqual(toDaysOffsetStr(25), "Vingt-cinq jours apr??s")

    def testHumanReadableJoin(self):
        self.assertEqual(hrJoin([""]), "")
        self.assertEqual(hrJoin (["glace"]), "glace")
        self.assertEqual(hrJoin (["glace", "feu"]), "glace et feu")
        self.assertEqual(hrJoin (["vent", "glace", "feu"]),
                         "vent, glace et feu")
        self.assertEqual(hrJoin (["chien", "chat", "poule", "yak", "fourmi"]),
                         "chien, chat, poule, yak et fourmi")

# ------------------------------------------------------------------------------
class  Test????????????????(TestCase):
    def setUp(self):
        translation.activate('el')

    def tearDown(self):
        translation.deactivate()

    def testToOrdinal(self):
        self.assertEqual(toOrdinal(-1), "????????????????????")
        self.assertEqual(toOrdinal(-2), "????????????????????????")
        self.assertEqual(toOrdinal (1), "??????????????????")
        self.assertEqual(toOrdinal (2), "????????????????????????")
        self.assertEqual(toOrdinal (3), "??????????")
        self.assertEqual(toOrdinal (4), "??????????????")
        self.assertEqual(toOrdinal (5), "??????????")

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
