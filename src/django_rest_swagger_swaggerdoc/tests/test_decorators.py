# -*- coding: utf-8 -*-
import unittest


class SwaggerDocDecoratorTest(unittest.TestCase):
    def test_it(self):
        from ..decorators import swaggerdoc

        @swaggerdoc('./swagger_test_doc.yml')
        def _test_fview_func(request):
            pass

        swagger_doc = getattr(_test_fview_func, '__swaggerdoc__')
        self.assertIsInstance(swagger_doc, dict)

    def test_view_exec(self):
        from django.test.client import RequestFactory
        from ..decorators import swaggerdoc

        @swaggerdoc('./swagger_test_doc.yml')
        def _test_fview_func(request):
            pass

        request_factory = RequestFactory()
        request = request_factory.get('/')
        _test_fview_func(request)
