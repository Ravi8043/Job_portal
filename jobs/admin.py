from django.contrib import admin
from .models import JobPosting, JobApplication
# Register your models here.
admin.site.register(JobPosting)
admin.site.register(JobApplication)