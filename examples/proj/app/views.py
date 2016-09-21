from rest_framework.decorators import api_view
from rest_framework.views import APIView

from django_rest_swagger_swaggerdoc import swaggerdoc


@swaggerdoc('api_test_doc.yml')
@api_view()
def example_view(request):
    pass


class ExampleView(APIView):
    @swaggerdoc('./api_test_doc.yml')
    def get(self, request):
        pass
