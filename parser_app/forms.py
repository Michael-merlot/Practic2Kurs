from django import forms

class JobSearchForm(forms.Form):
    title = forms.CharField(label='Job Title', max_length=100, required=False)
    company = forms.CharField(label='Company', max_length=100, required=False)
    location = forms.CharField(label='Location', max_length=100, required=False)
    skills = forms.CharField(label='Skills', max_length=200, required=False)
