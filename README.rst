CMSplugin Linklist
==================

Django app to render a list of links with meta information and screenshots.

Please note that this repo contains the same code as cmsplugin-linklist.
We will remove the Link-model related code from that repo soon so that the
cmsplugin repo only contains the cmsplugin relevant code.


Prerequisites
-------------

You need at least the following packages in your virtualenv:

* Django 1.4
* South
* Filer
* Pillow or PIL
* Easy Thumbnails


Installation
------------

To get the latest stable release from PyPi::

    $ pip install django-linklist (not available at the moment)

To get the latest commit from GitHub::

    $ pip install -e git://github.com/bitmazk/django-linklist.git#egg=linklist

Add the app to your ``INSTALLED_APPS``::

    INSTALLED_APPS = [
        ...
        'django',
        'filer',
        'easy_thumbnails',
        'linklist',
    ]

Run the south migrations to create the app's database tables::

    $ ./manage.py migrate linklist


Usage
-----

Add links to your project via the Django admin.


Templatetags
------------

get_linklist
++++++++++++

Returns a number of links::

    {% load linklist_tags %}
    {% get_linklist 8 as linklist %}
    {% for link in linklist %}
        // YOur HTML markup
    {% endfor %}

If you are using the ``LinkCategory`` model, you can get the links for a
cateogry like so::

    {% get_linklist 8 category='slug' as linklist %}


Roadmap
-------

See the issue tracker for current and upcoming features.
