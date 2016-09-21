django-rest-swagger-swaggerdoc - Additional Document
====================================================

.. image:: https://circleci.com/gh/TakesxiSximada/django-rest-swagger-swaggerdoc.svg?style=svg
           :target: https://circleci.com/gh/TakesxiSximada/django-rest-swagger-swaggerdoc
           :alt: CircleCI Status

.. image:: https://codecov.io/gh/TakesxiSximada/django-rest-swagger-swaggerdoc/branch/master/graph/badge.svg
           :target: https://codecov.io/gh/TakesxiSximada/django-rest-swagger-swaggerdoc
           :alt: CodeCov Status

Django REST Swagger 2.0 has changed drastically. For example, you may not put a return code in YAML files.
This package provides functions to inject a swagger style yaml data to the django-rest-swagger's data.


How to use it
-------------

1. You create a swagger style yaml file.

   This YAML file is swagger style.

   ./api_test_doc.yml::

       get:
         description: test document
         responses:
           200:
             description: success
           400:
             description: bad request
             schema:
               type: json
             headers:
               Content-Type: application/json


2. You create api view function or ViewClass.

   The swaggerdoc decorator to specify the relative path from the file
   the view callable is defined.

   views.py::

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


Install
-------

::

   $ pip install django-rest-swagger-swaggerdoc


It is depends on djangorestframework(>= 3.4.7).
If older than version 3.7.4, it may not be able to correctly resolve the YAML path.


Other
-----

- PyPI: https://pypi.python.org/pypi/django-rest-swagger-swaggerdoc
- Github: https://github.com/TakesxiSximada/django-rest-swagger-swaggerdoc
- CircleCI: https://circleci.com/gh/TakesxiSximada/django-rest-swagger-swaggerdoc
- CodeCov: https://codecov.io/gh/TakesxiSximada/django-rest-swagger-swaggerdoc
