=====
Usage
=====

.. _Apache2 mod_http2: https://httpd.apache.org/docs/2.4/mod/mod_http2.html
.. _H2Push: https://httpd.apache.org/docs/2.4/mod/mod_http2.html#h2push
.. _django.template.context_processors.request: https://docs.djangoproject.com/en/1.10/ref/templates/api/#django-template-context-processors-request

To use django-static-push in a project where you want push assets over HTTP/2, add the ``StaticPush`` middleware to your
``settings.py`` file and include the `django.template.context_processors.request`_ context processor in your templating
configuration::

    MIDDLEWARE = [
        ...,
        'django_static_push.middleware.StaticPush',
    ]

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    ...,
                    'django.template.context_processors.request',
                    ...,
                ],
            },
        },
    ]

Now you can use the ``staticpush`` templatetag in your Django templates::

    {% load staticpush %}
    <link rel="stylesheet" href="{% staticpush 'some/file.css' %}"

Make sure that `Apache2 mod_http2`_ has been configured correctly for your webserver::

    <VirtualHost *:443>
        ...
        Protocols h2 http/1.1
        H2Push on
        ...
    </VirtualHost>

Each HTTP response will now carry a ``Link`` header as described in the `H2Push`_ documentation, causing Apache2 to send
all files included by the ``staticpush`` templatetag to the webbrowser.
