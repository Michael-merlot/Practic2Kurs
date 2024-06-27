
from django.db.models import Count
from django.shortcuts import render
from .models import JobVacancy
import requests

def fetch_jobs_from_hh(request):
    url = 'https://api.hh.ru/vacancies'
    params = {
        'text': 'Python developer',
        'area': 1,  # Москва
        'per_page': 10
    }
    response = requests.get(url, params=params)
    jobs = response.json().get('items', [])

    for job in jobs:
        JobVacancy.objects.update_or_create(
            title=job['name'],
            company=job['employer']['name'],
            location=job['area']['name'],
            defaults={
                'description': job['snippet'].get('requirement', ''),
                'requirements': job['snippet'].get('responsibility', ''),
                'conditions': job.get('schedule', {}).get('name', '')
            }
        )

    return render(request, 'parser_app/job_list.html', {'jobs': jobs})



def job_statistics(request):
    total_jobs = JobVacancy.objects.count()
    jobs_by_company = JobVacancy.objects.values('company').annotate(total=Count('company')).order_by('-total')

    return render(request, 'parser_app/job_statistics.html', {
        'total_jobs': total_jobs,
        'jobs_by_company': jobs_by_company,
    })

