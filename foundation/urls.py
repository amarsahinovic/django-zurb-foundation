from django.urls import re_path
from django.views.generic import TemplateView

# Test patern, renders Zurb Foundation default page using base template
urlpatterns = [
    re_path(r'^$',view=TemplateView.as_view(template_name="foundation/index.html"),
        name="foundation_index"),

    re_path(r'^scss/$',view=TemplateView.as_view(template_name="foundation/scss/index.html"),
        name="foundation_scss_index"),

    re_path(r'^icons/$',view=TemplateView.as_view(template_name="foundation/icons.html"),
        name="foundation_icons"),
]
