

from django.test import TestCase
from .models import JobVacancy

class JobVacancyModelTest(TestCase):

    def setUp(self):
        JobVacancy.objects.create(
            title="Python Developer",
            company="Example Company",
            location="Москва",
            description="Some description",
            requirements="Some requirements",
            conditions="Full-time"
        )

    def test_job_vacancy_creation(self):
        job = JobVacancy.objects.get(title="Python Developer")
        self.assertEqual(job.company, "Example Company")
        self.assertEqual(job.location, "Москва")
        self.assertEqual(job.description, "Some description")
        self.assertEqual(job.requirements, "Some requirements")
        self.assertEqual(job.conditions, "Full-time")

class JobVacancyViewTest(TestCase):

    def test_fetch_jobs_view(self):
        response = self.client.get('/parser/fetch-jobs/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Available Jobs")

