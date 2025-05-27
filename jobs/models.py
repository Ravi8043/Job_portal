from django.db import models
from users.models import CustomUserModel
# Create your models here.

class JobPosting(models.Model):
    JOBTYPE_CHOICES = (
        ('full time','Full Time'),
        ('part time','Part Time')
    )
    JOBLOCATION_CHOICES = (
        ('remote','Remote'),
        ('city','City'),
        ('hybrid','Hybrid')
    )
    #we've to establish the relation between JobPosting and our CustomUserModel
    #coz most of the data we're taking from the user model
    posted_by = models.ForeignKey(
    CustomUserModel,
    on_delete=models.CASCADE,
    related_name='job_postings'
)
    job_role = models.CharField(max_length=50)
    skills_required = models.TextField(null=True, blank=True, help_text='skills required')
    description = models.TextField(null=True, blank=True, help_text='describe about job more')
    experience_required = models.IntegerField()
    job_type = models.CharField(choices=JOBTYPE_CHOICES)
    job_location_type = models.CharField(choices=JOBLOCATION_CHOICES)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.job_role



# models.py

class JobApplication(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )
    applied_by = models.ForeignKey(
        CustomUserModel,
        on_delete=models.CASCADE,
        related_name='job_applications'
    )
    job_role = models.ForeignKey(JobPosting, on_delete=models.CASCADE, related_name='application')
    resume = models.FileField(null=True, blank=True)
    cover_letter = models.FileField(null=True, blank=True)
    portfolio_link = models.URLField(null=True, blank=True)
    github_link = models.URLField(null=True, blank=True)
    linkedin_link = models.URLField(null=True, blank=True)
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.applied_by.username} - {self.job_role.job_role} ({self.status})"
 
class Notification(models.Model):
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name="notifications")
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"To {self.user.username}: {self.message[:50]}"