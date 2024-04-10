from django.urls import path
from .views import *


urlpatterns = [
    path('manage', manage_page, name='manage'),
]
