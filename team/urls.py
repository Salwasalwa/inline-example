from django.conf.urls import url

from .views import TeamCreateView

urlpatterns = [
    url(r'^new$', TeamCreateView.as_view(), name="team-new"),
]
