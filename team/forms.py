from django.forms import inlineformset_factory
from .models import *


TeamMateInlineFormset = inlineformset_factory(Team, TeamMate, fields="__all__", min_num=3, extra=1)
