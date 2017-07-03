# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import CreateView

from .models import Team
from .forms import TeamMateInlineFormset


class TeamCreateView(CreateView):
    model = Team
    fields = ('name', 'sport') # "__all__"
    success_url = "/team/new/"

    def get_context_data(self):
        context = CreateView.get_context_data(self)
        context["team_formset"] = TeamMateInlineFormset()
        return context

    def form_valid(self, form):
        team_resp = CreateView.form_valid(self, form)
        team_formset = TeamMateInlineFormset(self.request.POST, instance=self.object)

        if team_formset.is_valid():
            team_formset.save()

        return team_resp
