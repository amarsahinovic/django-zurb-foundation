django-zurb-foundation 6.2.3
============================

Django Zurb Foundation 6 package.

Version of this package is equal to the version of Zurb Foundation it provides.

Usage
=====

- Add `foundation` to your `INSTALLED_APPS`.
- If you want to use the provided base template, extend from `foundation/base.html`. If you want to write one from scratch, see the example template.
- If you want to test if foundation works, include `foundation.urls` in your urls.py and visit the path. You should see the Foundation test page.

Changes
=======
Version 6.2.3
- Updated foundation to 6.2.3 (codywd)

Version 5.5.0
- Updated foundation to 5.5.0

Version 5.4.7
- Updated foundation to 5.4.7

Version 5.4.5
- Updated foundation to 5.4.5

Version 5.3.0.1
- Added scss files

Version 5.3.0
- Updated foundation to 5.3.0
- Deprecated foundation tags (they will be removed in version 6.x)
- Updated templates not to use tags

Version 5.1.1
- Updated foundation to 5.1.1

Version 5.0.3

- Moved `js/modernizr` to `js/vendor/modernizr` and removed `js/vendor/custom.modernizr`
- Moved `js/jquery` to `js/vendor/jquery`

Version 5.0.2

- Renamed `foundation_body` to `base_body`
- Removed zepto and renamed `foundation_jquery_zepto` block to `foundation_jquery`
- Included foundation icons
- Renamed `foundation_include` to `foundation_js`
- Added `foundation_vendor` and `foundation_css` tags
- Used the tags from this package in the base template


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/amarsahinovic/django-zurb-foundation/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

