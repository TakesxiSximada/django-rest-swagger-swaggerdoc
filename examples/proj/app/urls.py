from django.conf.urls import url

from . import views

urlpatterns = [
    url('example1', views.example_view),
    url('example2', views.ExampleView.as_view()),
]
