from django.shortcuts import render
from . import serializers
from . import models
from rest_framework import viewsets
from . import permissions
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models.query import QuerySet
from typing import Any
from .models import Notification


# Create your views here.
class IsRecruiter(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False   
        if getattr(user, 'is_superuser', False):
            return True    
        return getattr(user, 'role', None) == 'recruiter'  

    def has_object_permission(self, request, view, obj):
        # For job postings, only allow access if the recruiter owns the job
        if hasattr(obj, 'recruiter'):
            return obj.recruiter == request.user or request.user.is_superuser
        return self.has_permission(request, view)  


class IsApplicant(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False   
        if getattr(user, 'is_superuser', False):
            return True    
        return getattr(user, 'role', None) == 'applicant' 

    def has_object_permission(self, request, view, obj):
        # For job applications, only allow access if the applicant owns the application
        if hasattr(obj, 'applicant'):
            return obj.applicant == request.user or request.user.is_superuser
        return self.has_permission(request, view)

class JobPostingView(viewsets.ModelViewSet):
    permission_classes = [IsRecruiter]
    queryset = models.JobPosting.objects.all()
    serializer_class = serializers.JobPostingSerializer
    #as we're not taking posted_by input from the user and need not to
    #coz it stores the loggin details which user already provided
    #so we manually override that posted_by using perform_create fn
    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)  # Crucial line
    

class JobApplicationView(viewsets.ModelViewSet):
    permission_classes = [IsApplicant]
    queryset = models.JobApplication.objects.all()
    serializer_class = serializers.JobApplicationSerializer
    def perform_create(self, serializer):
        serializer.save(applied_by=self.request.user)  # Crucial line
    

class RecruiterNotificationView(generics.GenericAPIView):
    serializer_class = serializers.NotificationSerializer
    permission_classes = [IsRecruiter]

    def get_queryset(self) -> Any:
        return Notification.objects.filter(user=self.request.user).order_by('-created_at')

    def get(self, request, *args, **kwargs):
        notifications = self.get_queryset()
        serializer = self.get_serializer(notifications, many=True)
        return Response(serializer.data)
class JobApplicationStatusUpdateView(generics.UpdateAPIView):
    queryset = models.JobApplication.objects.all()
    serializer_class = serializers.JobApplicationStatusSerializer
    permission_classes = [IsRecruiter]
class ApplicantDashboardView(generics.ListAPIView):
    serializer_class = serializers.JobApplicationSerializer
    permission_classes = [IsApplicant]

    def get_queryset(self) -> Any:
        return models.JobApplication.objects.filter(applied_by=self.request.user).order_by('-id')