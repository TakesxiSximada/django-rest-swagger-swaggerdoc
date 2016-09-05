# -*- coding: utf-8 -*-

import logging
import rest_framework_swagger.renderers as rest_swagger_renderers

from django.core import urlresolvers
from zope.dottedname import resolve


logger = logging.getLogger(__name__)


def resolve_swagger_doc(url, method):
    resolve_result = urlresolvers.resolve(url)
    swaggerdoc = getattr(resolve_result.func, '__swaggerdoc__', None)
    if swaggerdoc:
        return swaggerdoc

    view_class = resolve.resolve(resolve_result.view_name)
    view = getattr(view_class, method.lower(), None)
    return getattr(view, '__swaggerdoc__', None)


def overwrite_data(url, method, data, swaggerdoc):
    additional_data = dict(swaggerdoc).get(method, {})
    try:
        data['paths'][url][method].update(additional_data)
    except (KeyError, TypeError, AttributeError) as err:
        logger.debug('Cannot update swagger data: %r', err)


class SwaggerAdditinalDocRenderer(rest_swagger_renderers.OpenAPIRenderer):
    def add_customizations(self, data, renderer_context):
        super(SwaggerAdditinalDocRenderer, self).add_customizations(
            data, renderer_context)
        for url, path in data['paths'].items():
            for method, method_data in path.items():
                swaggerdoc = resolve_swagger_doc(url, method)
                if swaggerdoc:
                    overwrite_data(url, method, data, swaggerdoc)
