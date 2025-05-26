from django.contrib import admin
from .models import JobPosting, JobApplication, Notification
# Register your models here.
admin.site.register(JobPosting)
admin.site.register(JobApplication)
admin.site.register(Notification)