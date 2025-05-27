from rest_framework import serializers
from . import models


class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JobPosting
        fields = [
            'job_role','skills_required','description','experience_required',
            'job_type','job_location_type','is_active',
        ]
        read_only_fields = ['posted_by']
class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JobApplication
        fields = [
            'job_role','resume','cover_letter','portfolio_link','github_link','linkedin_link','status',
        ]
        read_only_fields = ['applied_by',]


class NotificationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = models.Notification
        fields = ['id', 'user', 'username', 'message', 'is_read', 'created_at']
        read_only_fields = ['id', 'user', 'username', 'message', 'created_at']

class JobApplicationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JobApplication
        fields = ['status']