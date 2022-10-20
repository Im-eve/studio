from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='pIndex'),
    path('project/', project, name='pProject'),
]
