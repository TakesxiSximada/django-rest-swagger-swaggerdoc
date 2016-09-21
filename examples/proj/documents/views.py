from rest_framework_swagger.renderers import SwaggerUIRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import response, schemas

from django_rest_swagger_swaggerdoc.renderers import SwaggerAdditinalDocRenderer


@api_view()
@renderer_classes([SwaggerUIRenderer, SwaggerAdditinalDocRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='Pastebin API')
    return response.Response(generator.get_schema(request=request))
