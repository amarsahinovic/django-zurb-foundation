from django import template
from django.templatetags.static import static

register = template.Library()

@register.simple_tag
def foundation_include(js_name):
    js_path = "foundation/js/foundation/foundation.{0}.js".format(js_name)
    return '<script src="{0}"></script>'.format(static(js_path))
