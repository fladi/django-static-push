# -*- coding: utf-8 -*-

import hashlib
import hmac
import json
import unittest

from django.core.exceptions import ImproperlyConfigured
from django.http import (
    HttpResponse
)
from django.template import Context, RequestContext, Template
from django.test import RequestFactory
from django.views.generic import View

from django_static_push.middleware import StaticPush


class TestTag(unittest.TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_get_path(self):
        class TagView(View):
            t = Template('{% load staticpush %}{% staticpush "foo.png" %}')

            def get(self, request):
                c = RequestContext(request, {})
                return HttpResponse(self.t.render(c))

        mw = StaticPush(TagView.as_view())
        request = self.factory.get('/fake')
        response = mw(request)
        self.assertIn('Link', response)
        self.assertEqual('</static/foo.png>;rel=preload', response['Link'])

    def test_get_variable(self):
        class TagView(View):
            t = Template('{% load staticpush %}{% staticpush file %}')

            def get(self, request):
                c = RequestContext(request, {'file': 'file.png'})
                return HttpResponse(self.t.render(c))

        mw = StaticPush(TagView.as_view())
        request = self.factory.get('/fake')
        response = mw(request)
        self.assertIn('Link', response)
        self.assertEqual('</static/file.png>;rel=preload', response['Link'])

    def test_no_request(self):
        class TagView(View):
            t = Template('{% load staticpush %}{% staticpush file %}')

            def get(self, request):
                c = Context()
                return HttpResponse(self.t.render(c))

        mw = StaticPush(TagView.as_view())
        request = self.factory.get('/fake')
        response = mw(request)
        self.assertNotIn('Link', response)
