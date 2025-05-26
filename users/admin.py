from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.CustomUserModel)
admin.site.register(models.RecruiterProfile)
admin.site.register(models.ApplicantProfile)