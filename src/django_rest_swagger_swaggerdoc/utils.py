# -*- coding: utf-8 -*-
import os
import inspect

from . import exc


def get_caller_module(depth=0):
    dotted = module = path = dirpath = None
    frame = inspect.currentframe().f_back.f_back
    for ii in range(depth):
        frame = frame.f_back
    dotted = frame.f_globals['__name__']
    fromlist = []
    if dotted.count('.') > 0:  # sub module or sub package
        fromlist = '.'.join(dotted.split('.')[:-1])

    try:
        module = __import__(dotted, globals={}, locals={}, fromlist=fromlist)
    except ImportError:  # pragma: no cover
        raise exc.CallerModuleResolveError(
            'can not import module: dotted={}, frame={}'.format(dotted, frame))

    path = module.__file__
    dirpath = os.path.dirname(path)
    return dotted, module, path, dirpath
