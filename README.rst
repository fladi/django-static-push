========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        | |codecov|
    * - package
      - |version| |downloads| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/django-static-push/badge/?style=flat
    :target: https://readthedocs.org/projects/django-static-push
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/fladi/django-static-push.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/fladi/django-static-push

.. |requires| image:: https://requires.io/github/fladi/django-static-push/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/fladi/django-static-push/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/fladi/django-static-push/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/fladi/django-static-push

.. |version| image:: https://img.shields.io/pypi/v/django-static-push.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/django-static-push

.. |downloads| image:: https://img.shields.io/pypi/dm/django-static-push.svg?style=flat
    :alt: PyPI Package monthly downloads
    :target: https://pypi.python.org/pypi/django-static-push

.. |wheel| image:: https://img.shields.io/pypi/wheel/django-static-push.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/django-static-push

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/django-static-push.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/django-static-push

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/django-static-push.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/django-static-push


.. end-badges

Middleware and templatetag for Django to utilize HTTP/2 push for assets included in a Django template. The
middleware injects a `Link` header in each response if there are files to be pushed to the client. All files in the
template which are suitable for HTTP/2 push should be included with the ``staticpush`` templatetag instead of the
vanilla ``static`` templatetag. The former simply augments the later and registers the resulting static URL with the
middleware.

This package currently supports Apache2 webservers with ``mod_http2`` enabled, as the actual HTTP/2 push is offloaded to the
webserver.

.. warning::

    This is ALPHA code. Do not use in production! It only serves as a proof-of-concept for now.

    Conditional HTTP/2 push is not supported yet. This means that your site will actually perform worse than
    over HTTP/1.1 because each response will trigger a push of all incldued assets, irrespective of any cache on the
    webbrowser.

Installation
============

::

    pip install django-static-push

Documentation
=============

https://django-static-push.readthedocs.io/en/latest/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
