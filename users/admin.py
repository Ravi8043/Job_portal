from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
admin.site.register(models.CustomUserModel)
admin.site.register(models.RecruiterProfile)
admin.site.register(models.ApplicantProfile)
