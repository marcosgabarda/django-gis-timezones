# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division, absolute_import

from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.core.exceptions import ObjectDoesNotExist


class TimeZoneManager(models.GeoManager):

    def get_from_position(self, position):
        """Gets the timezone from latitude an longitude."""
        timezones = self.filter(shape__contains=Point(float(position[1]), float(position[0])))
        if not timezones.exists():
            raise ObjectDoesNotExist
        return timezones.first()
