from django.conf.urls import patterns
from django.views.generic import TemplateView

# Test patern, renders Zurb Foundation default page using base template
urlpatterns = patterns('',
    (r'^foundation/', TemplateView.as_view(template_name="foundation/index.html")),
)
