from django.conf.urls import url
from . import views

urlpatterns = [
    url('hey/', views.index, name='index'),
]

