from django.conf.urls import url

from . import views

urlpatterns = [
    url('example1', views.example1_view),
    url('example2', views.Example2View.as_view()),
]
