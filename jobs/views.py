from django.shortcuts import render
from . import serializers
from . import models
from rest_framework import viewsets
from . import permissions
from rest_framework.views import APIView
from rest_framework.response import Response


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
            print("you're not authenticated")
            return False   
        if getattr(user, 'is_superuser', False):
            print('you are a superuser')
            return True    
        print("🔎 Role: ", getattr(user, 'role', 'No role found'))
        return getattr(user, 'role', None) == 'applicant' 

    def has_object_permission(self, request, view, obj):
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
    
# class RecruiterNotificationsView(APIView):
#     def get(self, request):
#         if request.user.role != 'recruiter':
#             return Response({'error': 'Only recruiters can view this'}, status=403)

#         notifications = models.Notification.objects.filter(user=request.user).order_by('-created_at')
#         serializer = serializers.NotificationSerializer(notifications, many=True)
#         return Response(serializer.data)