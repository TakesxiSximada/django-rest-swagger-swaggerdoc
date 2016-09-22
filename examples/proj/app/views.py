from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from django_rest_swagger_swaggerdoc import swaggerdoc


@swaggerdoc('swaggerdoc/example1.yml')
@api_view()
def example1_view(request):
    return Response('example1')


class Example2View(APIView):
    @swaggerdoc('swaggerdoc/example2.yml')
    def get(self, request):
        return Response('example2')
