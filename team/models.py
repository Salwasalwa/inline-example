# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

SPORT_CHOICES = (
    ("FOOT", 'Football'),
    ("TENN", 'Tennis'),
    ("CURL", 'Curling'),
)


class Team(models.Model):
    name = models.CharField(max_length=150)
    sport = models.CharField(max_length=150, choices=SPORT_CHOICES)

    def __unicode__(self):
        return self.name


class TeamMate(models.Model):
    name = models.CharField(max_length=150)
    team = models.ForeignKey(Team)

    def __unicode__(self):
        return self.name
