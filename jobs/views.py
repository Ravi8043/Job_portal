from django.shortcuts import render
from . import serializers
from . import models
from rest_framework import viewsets
from . import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

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
        return self.has_permission(request, view)


class JobPostingView(viewsets.ModelViewSet):
    permission_classes = [IsRecruiter]
    queryset = models.JobPosting.objects.all()
    serializer_class = serializers.JobPostingSerializer
    

class JobApplicationView(viewsets.ModelViewSet):
    permission_classes = [IsApplicant]
    queryset = models.JobApplication.objects.all()
    serializer_class = serializers.JobApplicationSerializer
    
class RecruiterNotificationsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role != 'recruiter':
            return Response({'error': 'Only recruiters can view this'}, status=403)

        notifications = models.Notification.objects.filter(user=request.user).order_by('-created_at')
        serializer = serializers.NotificationSerializer(notifications, many=True)
        return Response(serializer.data)