from django.db.models import Count
from django.shortcuts import render
from .models import JobVacancy
from .forms import JobSearchForm
import requests

def fetch_jobs_from_hh(request):
    form = JobSearchForm(request.GET or None)
    jobs = []
    max_results = 100  # Максимальное количество вакансий для извлечения
    results_per_page = 50  # Количество вакансий на страницу

    if form.is_valid():
        params = {
            'text': form.cleaned_data.get('title', ''),
            'area': form.cleaned_data.get('location', ''),
            'per_page': results_per_page
        }

        for page in range(0, max_results // results_per_page):
            params['page'] = page
            print(f"Request parameters: {params}")  # Отладочное сообщение
            response = requests.get('https://api.hh.ru/vacancies', params=params)

            if response.status_code == 200:
                page_jobs = response.json().get('items', [])
                print(f"Fetched {len(page_jobs)} jobs from API on page {page}")  # Отладочное сообщение
                print(response.json())  # Печатаем весь ответ от API для проверки
                jobs.extend(page_jobs)
                for job in page_jobs:
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
            else:
                print(f"Error fetching data from API: {response.status_code}")  # Отладочное сообщение

    # Извлечение вакансий из базы данных с учётом фильтров
    db_jobs = JobVacancy.objects.all()
    if form.is_valid():
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



