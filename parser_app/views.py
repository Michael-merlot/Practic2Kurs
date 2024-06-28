from django.db.models import Count
from django.shortcuts import render
from .models import JobVacancy
from .forms import JobSearchForm
import requests


def fetch_jobs_from_hh(request):
    form = JobSearchForm(request.GET or None)
    jobs = []

    if form.is_valid():
        params = {
            'text': form.cleaned_data['title'],
            'area': form.cleaned_data['location'],
            'per_page': 10
        }
        response = requests.get('https://api.hh.ru/vacancies', params=params)

        if response.status_code == 200:
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

        print(f"Fetched {len(jobs)} jobs from API")

    # Извлечение вакансий из базы данных с учётом фильтров
    db_jobs = JobVacancy.objects.all()
    if form.cleaned_data['title']:
        db_jobs = db_jobs.filter(title__icontains=form.cleaned_data['title'])
    if form.cleaned_data['company']:
        db_jobs = db_jobs.filter(company__icontains=form.cleaned_data['company'])
    if form.cleaned_data['location']:
        db_jobs = db_jobs.filter(location__icontains=form.cleaned_data['location'])
    if form.cleaned_data['skills']:
        db_jobs = db_jobs.filter(description__icontains=form.cleaned_data['skills'])

    return render(request, 'parser_app/job_list.html', {'form': form, 'jobs': db_jobs})



def job_statistics(request):
    total_jobs = JobVacancy.objects.count()
    jobs_by_company = JobVacancy.objects.values('company').annotate(total=Count('company')).order_by('-total')

    return render(request, 'parser_app/job_statistics.html', {
        'total_jobs': total_jobs,
        'jobs_by_company': jobs_by_company,
    })



