from rest_framework import routers
from . import views
from django.urls import path

router = routers.SimpleRouter()
router.register('jobs', views.JobPostingView, basename='jobs')
router.register('jobapply', views.JobApplicationView, basename='job_apply')

urlpatterns = router.urls + [
    path('recruiter/notifications/', views.RecruiterNotificationView.as_view(), name='recruiter-notifications'),
    path('recruiter/jobapplication/<int:pk>/status/', views.JobApplicationStatusUpdateView.as_view(), name='update-application-status'),
    path('applicant/dashboard/', views.ApplicantDashboardView.as_view(), name='applicant-dashboard'),
]
