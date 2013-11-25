from django import template
from django.templatetags.static import static

register = template.Library()

@register.simple_tag
def foundation_js(js_name=None):
    js_path = "foundation/js/foundation/foundation.{0}.js".format(js_name)
    if js_name is None:
       js_path = "foundation/js/foundation.min.js".format(js_name)

    return '<script src="{0}"></script>'.format(static(js_path))

@register.simple_tag
def foundation_vendor(vendor_name):
    vendor_path = "foundation/js/vendor/{0}.js".format(vendor_name)
    return '<script src="{0}"></script>'.format(static(vendor_path))

@register.simple_tag
def foundation_css(css_name):
    css_path = "foundation/css/{0}.css".format(css_name)
    return '<link rel="stylesheet" href="{0}"/>'.format(static(css_path))
