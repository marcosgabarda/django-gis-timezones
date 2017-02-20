# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division, absolute_import

from belt.models import GisTimeStampedModel
from django.contrib.gis.db import models
from django.utils.encoding import python_2_unicode_compatible

from gis_timezones.managers import TimeZoneManager


@python_2_unicode_compatible
class TimeZone(GisTimeStampedModel):
    """TimeZone GIS model, to obtain the timezone name using
    the a pair of coordinates.
    """

    name = models.CharField(max_length=250)
    shape = models.GeometryField()

    objects = TimeZoneManager()

    def __str__(self):
        return self.name
