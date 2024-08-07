from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import ProfileInfo, EducationInfo, JobInfo


# Create your views here.
# my personal details
class HomeView(TemplateView):
    model = ProfileInfo
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the ProfileInfo object (assuming there is only one)
        profile_info = ProfileInfo.objects.first()  # Adjust query as needed
        context['profile_info'] = profile_info
        return context


# my educational background
class EduView(ListView):
    model = EducationInfo
    template_name = 'Education.html'
    context_object_name = 'edu_info'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edu_info'] = EducationInfo.objects.first()
        return context


class JobView(ListView):
    model = JobInfo
    template_name = 'job.html'
    context_object_name = 'job_info'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['job_info'] = JobInfo.objects.first()
        return context


class ContactView(TemplateView):
    template_name = 'contact.html'