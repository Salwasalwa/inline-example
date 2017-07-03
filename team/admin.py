# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *


class TeamMateInline(admin.TabularInline):
    model = TeamMate

class TeamAdmin(admin.ModelAdmin):
    inlines = [
        TeamMateInline,
    ]


admin.site.register(Team, TeamAdmin)
admin.site.register(TeamMate)
