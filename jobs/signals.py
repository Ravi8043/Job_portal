# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import JobApplication, Notification

@receiver(post_save, sender=JobApplication)
def notify_recruiter_on_application(sender, instance, created, **kwargs):
    if created:
        job = instance.job_role  
        recruiter = job.posted_by  
        applicant = instance.applied_by  

        Notification.objects.create(
            user=recruiter,
            message=f"{applicant.username} applied for your job: {job.job_role}"
        )
