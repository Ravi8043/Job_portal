from django.db import models
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
    job_role = models.CharField(max_length=50)
    skills_required = models.TextField(null=True, blank=True, help_text='skills required')
    description = models.TextField(null=True, blank=True, help_text='describe about job more')
    experience_required = models.IntegerField()
    job_type = models.CharField(choices=JOBTYPE_CHOICES)
    job_location_type = models.CharField(choices=JOBLOCATION_CHOICES)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.job_role



class JobApplication(models.Model):
    job_role = models.ForeignKey(JobPosting, on_delete=models.CASCADE, related_name='application')
    resume = models.FileField(null=True, blank=True)
    cover_letter = models.FileField(null=True, blank=True)
    portfolio_link = models.URLField(null=True, blank=True)
    github_link = models.URLField(null=True, blank=True)
    linkedin_link = models.URLField(null=True, blank=True)