# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import JobApplication, Notification  # Update to your actual model imports

@receiver(post_save, sender=JobApplication)
def notify_recruiter_on_application(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.job.recruiter,
            message=f"{instance.applicant.user.username} applied for your job: {instance.job.title}"
        )

@receiver(post_save, sender=JobApplication)
def notify_applicant_on_status_update(sender, instance, created, **kwargs):
    if not created:  # If it's an update
        Notification.objects.create(
            user=instance.applicant.user,
            message=f"Your application for {instance.job.title} is now: {instance.status}"
        )
