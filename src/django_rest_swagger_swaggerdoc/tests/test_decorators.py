# -*- coding: utf-8 -*-
import unittest

from . import compat


class SwaggerDocDecoratorTest(unittest.TestCase):
    def _get_target(self):
        from ..decorators import swaggerdoc as target
        return target

    def test_it(self):
        target = self._get_target()
        deco = target('./swagger_test_doc.yml')
        func = compat.mock.Mock()
        wrapped_func = deco(func)
        swagger_doc = getattr(wrapped_func, '__swaggerdoc__')
        self.assertIsInstance(swagger_doc, dict)
