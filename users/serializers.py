from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import CustomUserModel, RecruiterProfile, ApplicantProfile
from typing import Any

class CustomRegisterSerializer(RegisterSerializer):
    role = serializers.ChoiceField(choices=CustomUserModel.ROLE_CHOICES)

    # Fields for Recruiter
    company_name = serializers.CharField(required=False)
    #these are not required here coz validation handling in the upcoming logic
    linkedin_url = serializers.URLField(required=False)

    # Fields for Applicant
    skills = serializers.CharField(required=False)
    github_link = serializers.URLField(required=False)
    portfolio_link = serializers.URLField(required=False)

    def get_cleaned_data(self, *args, **kwargs) -> dict[str, Any]:
        data = super().get_cleaned_data()
        validated_data = getattr(self, 'validated_data', {}) or {}
        if isinstance(validated_data, dict):
            data['role'] = validated_data.get('role', '')
        return data

    def custom_signup(self, request, user, *args, **kwargs):
        validated_data = getattr(self, 'validated_data', {}) or {}

        if not isinstance(validated_data, dict):
            return  # Just exit if data isn't valid dict

        role = validated_data.get('role')

        if role == 'recruiter':
            RecruiterProfile.objects.create(
                user=user,
                company_name=validated_data.get('company_name', ''),
                linkedin_url=validated_data.get('linkedin_url', '')
            )
        elif role == 'applicant':
            ApplicantProfile.objects.create(
                user=user,
                skills=validated_data.get('skills', ''),
                github_link=validated_data.get('github_link', ''),
                portfolio_link=validated_data.get('portfolio_link', '')
            )