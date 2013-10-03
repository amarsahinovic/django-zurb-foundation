django-zurb-foundation 4.3.2
============================

Django Zurb Foundation 4 package.

Version of this package is equal to the version of Zurb Foundation it provides.

Usage
=====

- Add `foundation` to your INSTALLED_APPS.
- If you want to use the provided base template, extend from `foundation/base.html`. If you want to write one from scratch, see the example template.
- If you want to test if foundation works, include `foundation.urls` in your urls.py and visit the path. You should see the Foundation test page.

Including Zurb Foundation JS files
==================================

To include additional Zurb Foundation JS files, you can use `foundation_include` tag. 

For example, to include `abide` library use:

    {% foundation_include 'abide' %}

Depending on your static url, it will replace the previous tag with something like `<script src="/static/foundation/js/foundation/foundation.abide.js"></script>`.
You can see example usage in `index.html` template.

TODO
====

- Improve default template
- Document the default template better

