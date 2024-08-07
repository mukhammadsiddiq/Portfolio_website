from django.contrib import admin
from .models import ProfileInfo, EducationInfo, JobInfo
# Register your models here.
admin.site.register(ProfileInfo)
admin.site.register(EducationInfo)
admin.site.register(JobInfo)