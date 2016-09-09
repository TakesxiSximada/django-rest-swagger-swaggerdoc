import unittest


class GetCallerModuleTest(unittest.TestCase):
    def _get_target(self):
        from ..utils import get_caller_module as target
        return target

    def _call_func(self, *args, **kwds):
        target = self._get_target()
        return target(*args, **kwds)

    def test_depth(self):
        self._call_func(depth=2)

    def test_it(self):
        import os
        from zope.dottedname.resolve import resolve

        module_name = 'django_rest_swagger_swaggerdoc.tests.test_utils'
        module = resolve(module_name)
        module_path = os.path.abspath(module.__file__)
        module_dir = os.path.dirname(module_path)

        res = self._call_func()
        self.assertEqual(res[0], module_name)
        self.assertEqual(res[1], module)
        self.assertEqual(res[2], module_path)
        self.assertEqual(res[3], module_dir)
