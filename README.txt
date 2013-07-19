django-zurb-foundation
======================

Django Zurb Foundation package.

Version of this package is equal to the version of Zurb Foundation it provides.

Usage
=====

- Add 'foundation' to your INSTALLED_APPS
- If you want to use the provided base template, extend from 'foundation/base.html'. If you want to write one from scratch, see the example template.
- If you want to test if foundation works, include 'foundation.urls' to your urls.py and visit the path. You should see the foundation test page.

TODO
====

- Improve default template
- Write template tags for easier inclusion of static files in custom templates
- Document the default template better
