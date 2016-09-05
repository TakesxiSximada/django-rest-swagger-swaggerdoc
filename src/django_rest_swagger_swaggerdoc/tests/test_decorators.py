# -*- coding: utf-8 -*-
import unittest


class SwaggerDocDecoratorTest(unittest.TestCase):
    def _get_target(self):
        from ..decorators import swaggerdoc as target
        return target

    def test_it(self):

        def _test_fview_func(request):
            pass

        target = self._get_target()
        deco = target('./swagger_test_doc.yml')
        wrapped_func = deco(_test_fview_func)
        swagger_doc = getattr(wrapped_func, '__swaggerdoc__')
        self.assertIsInstance(swagger_doc, dict)
