from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUserModel(AbstractUser):
    ROLE_CHOICES = (
        ('applicant','applicant'),
        ('recruiter','recruiter')
    )
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    role = models.CharField(max_length=20,choices=ROLE_CHOICES)
    
    def __str__(self):
        return self.username

class RecruiterProfile(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, primary_key=True, related_name='recruiter_profile')
    company_name = models.CharField(max_length=20)
    company_email = models.EmailField(null=True, blank=True)
    role_in_company = models.CharField(max_length=20)
    linkedin_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class ApplicantProfile(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, primary_key=True, related_name='applicant_profile')
    skills = models.TextField(null=True, blank=True)
    github_link = models.URLField(null=True, blank=True)
    portfolio_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.user.username