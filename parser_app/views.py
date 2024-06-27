# parser_app/views.py

from django.shortcuts import render
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
    return render(request, 'parser_app/job_list.html', {'jobs': jobs})
