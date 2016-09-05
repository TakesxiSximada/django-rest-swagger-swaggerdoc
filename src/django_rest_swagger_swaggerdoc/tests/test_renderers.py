# -*- coding: utf-8 -*-
import unittest


class SwaggerAdditinalDocRendererTest(unittest.TestCase):
    def _get_target(self):
        from ..renderers import SwaggerAdditinalDocRenderer as target
        return target

    def _make_one(self, *args, **kwds):
        target = self._get_target()
        return target(*args, **kwds)

    def test_it(self):
        from django.test.client import RequestFactory

        request_factory = RequestFactory()
        context = {
            'request': request_factory.get('/')
        }
        data = {
            'paths': {},
        }

        renderer = self._make_one()
        renderer.add_customizations(data, context)
