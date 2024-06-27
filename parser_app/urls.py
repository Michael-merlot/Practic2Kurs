# parser_app/urls.py

from django.urls import path
from .views import fetch_jobs_from_hh

urlpatterns = [
    path('fetch-jobs/', fetch_jobs_from_hh, name='fetch_jobs'),
]
