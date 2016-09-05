# -*- coding: utf-8 -*-
import os
import unittest

import rest_framework.decorators as rest_decorators
import rest_framework.views as rest_views

from .compat import mock
from .. import decorators

here = os.path.dirname(os.path.abspath(__file__))

# =================== TEST VIEW ================================================


@decorators.swaggerdoc('swagger_test_doc.yml')
@rest_decorators.api_view()
def example_view(request):
    pass


class ExampleView(rest_views.APIView):
    @decorators.swaggerdoc('swagger_test_doc.yml')
    def get(self, request):
        pass

# ==============================================================================


class SwaggerDocResulveTest(unittest.TestCase):

    def _call_fut(self, *args, **kwds):
        from ..renderers import resolve_swagger_doc as target
        return target(*args, **kwds)

    @mock.patch('django.core.urlresolvers.resolve')
    def test_func_style_view(self, resolve):
        from django.urls import ResolverMatch
        from ..documents import SwaggerDoc

        resulve_match = ResolverMatch(func=example_view, args=[], kwargs={})

        resolve.return_value = resulve_match

        swagger_doc = self._call_fut(url='/', method='get')
        self.assertIsInstance(swagger_doc, SwaggerDoc)

    @mock.patch('django.core.urlresolvers.resolve')
    def test_class_style_view(self, resolve):
        from django.urls import ResolverMatch
        from ..documents import SwaggerDoc

        view = ExampleView()
        resulve_match = ResolverMatch(func=view.get, args=[], kwargs={})
        resulve_match.func_name = '{}.{}'.format(
            ExampleView.__module__, ExampleView.__name__)
        resolve.return_value = resulve_match

        swagger_doc = self._call_fut(url='/', method='get')
        self.assertIsInstance(swagger_doc, SwaggerDoc)

    @mock.patch('django.core.urlresolvers.resolve')
    @mock.patch('zope.dottedname.resolve.resolve')
    def test_cannnot_to_get_swaggerdoc(self, zope_resolve, dj_resolve):
        from django.urls import ResolverMatch

        resulve_match = ResolverMatch(func=None, args=[], kwargs={})
        dj_resolve.return_value = resulve_match
        zope_resolve.return_value = None
        swagger_doc = self._call_fut(url='/', method='get')
        self.assertIsNone(swagger_doc)


class OverwriteDataTest(unittest.TestCase):
    def _call_fut(self, *args, **kwds):
        from ..renderers import overwrite_data
        return overwrite_data(*args, **kwds)

    def test_it(self):
        from ..documents import SwaggerDoc
        data = {
            'paths': {
                '/': {
                    'get': {},
                }
            }
        }

        swagger_doc = SwaggerDoc()
        swagger_doc['get'] = {
            'description': 'test description',
        }
        self._call_fut(url='/', method='get', data=data, swaggerdoc=swagger_doc)
        self.assertEqual(data['paths']['/']['get']['description'], 'test description')

    def test_ignore_key_error(self):
        from ..documents import SwaggerDoc
        data = {
            'paths': {
            }
        }

        swagger_doc = SwaggerDoc()
        swagger_doc['get'] = {
            'description': 'test description',
        }

        self._call_fut(url='/', method='get', data=data, swaggerdoc=swagger_doc)

    def test_ignore_type_error(self):
        from ..documents import SwaggerDoc
        data = {
            'paths': {
                '/': {
                    'get': None
                }
            }
        }

        swagger_doc = SwaggerDoc()
        swagger_doc['get'] = {
            'description': 'test description',
        }

        self._call_fut(url='/', method='get', data=data, swaggerdoc=swagger_doc)


class SwaggerAdditinalDocRendererTest(unittest.TestCase):
    def _get_target(self):
        from ..renderers import SwaggerAdditinalDocRenderer as target
        return target

    def _make_one(self, *args, **kwds):
        target = self._get_target()
        return target(*args, **kwds)

    @mock.patch('django_rest_swagger_swaggerdoc.renderers.resolve_swagger_doc')
    def test_it(self, resolve_swagger_doc):
        from django.test.client import RequestFactory
        from ..documents import SwaggerDoc

        swagger_doc = SwaggerDoc()
        swagger_yml_path = os.path.join(here, 'swagger_test_doc.yml')
        swagger_doc.load_yaml(swagger_yml_path)
        resolve_swagger_doc.return_value = swagger_doc

        request_factory = RequestFactory()
        context = {
            'request': request_factory.get('/')
        }
        data = {
            'paths': {
                '/': {
                    'get': {
                    },
                },
            },
        }
        renderer = self._make_one()

        renderer.add_customizations(data, context)
        self.assertEqual(data['paths']['/']['get']['description'], 'test document')
