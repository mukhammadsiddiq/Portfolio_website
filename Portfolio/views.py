from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import ProfileInfo, EducationInfo


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
class EduView(TemplateView):
    template_name = 'Education.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        edu_info =EducationInfo.objects.first()
        context['edu_info'] = edu_info
        return context


class JobView(DetailView):
    template_name = 'job.html'


class ContactView(TemplateView):
    template_name = 'contact.html'