from django.db import models

class JobSeeker(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    skills = models.TextField()
    experience = models.TextField()
    education = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class JobVacancy(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200, default='Unknown')  # Значение по умолчанию
    description = models.TextField()
    requirements = models.TextField()
    conditions = models.TextField()

    def __str__(self):
        return self.title
