from django.contrib import admin
from .models import ProfileInfo, EducationInfo, JobInfo, PartTime
# Register your models here.
admin.site.register(ProfileInfo)
admin.site.register(EducationInfo)
admin.site.register(JobInfo)
admin.site.register(PartTime)