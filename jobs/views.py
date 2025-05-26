from django.shortcuts import render
from . import serializers
from . import models
from rest_framework import viewsets

# Create your views here.
class JobPostingView(viewsets.ModelViewSet):
    queryset = models.JobPosting.objects.all()
    serializer_class = serializers.JobPostingSerializer

class JobApplicationView(viewsets.ModelViewSet):
    queryset = models.JobApplication.objects.all()
    serializer_class = serializers.JobApplicationSerializer