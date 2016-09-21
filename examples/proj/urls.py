from django.conf.urls import url, include

from .documents import urls as documents_urls
from .app import urls as app_urls

urlpatterns = [
    url('documents', include(documents_urls)),
    url('app', include(app_urls))
]
