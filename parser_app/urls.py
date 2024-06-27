
from django.urls import path
from .views import fetch_jobs_from_hh, job_statistics

urlpatterns = [
    path('fetch-jobs/', fetch_jobs_from_hh, name='fetch_jobs'),
    path('job-statistics/', job_statistics, name='job_statistics'),
]

