from rest_framework import serializers
from . import models

class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JobPosting
        fields = [
            'job_role','skills_required','description','experience_required',
            'job_type','job_location_type','is_active',
        ]

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JobApplication
        fields = [
            'job_role','resume','cover_letter','portfolio_link','github_link','linkedin_link',
        ]