# -*- coding: utf-8 -*-
import os
import functools

from . import documents
from . import utils


def swaggerdoc(doc_path):
    def _inner(func):
        @functools.wraps(func)
        def _wrap(*args, **kwds):
            return func(*args, **kwds)

        swagger_doc = documents.SwaggerDoc()

        dotted, module, path, dirpath = utils.get_caller_module()
        doc_abs_path = os.path.join(os.path.join(dirpath, doc_path))
        swagger_doc.load_yaml(doc_abs_path)
        setattr(_wrap, '__swaggerdoc__', swagger_doc)
        return _wrap
    return _inner
