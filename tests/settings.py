# -*- coding: utf-8 -*-

INSTALLED_APPS = [
    'django_static_push',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request'
            ]
        },
    },
]

STATIC_URL = '/static/'

SECRET_KEY = 'an9)lb_asn(6ri6++ic_fat5%e&6y_t*0l9u&a27!bald=gflw'

ROOT_URLCONF = 'tests.urls'
