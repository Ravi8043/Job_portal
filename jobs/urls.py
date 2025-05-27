from rest_framework import routers
from . import views
from django.urls import path
router = routers.SimpleRouter()

router.register('jobs',views.JobPostingView, basename='jobs')
router.register('jobapply',views.JobApplicationView, basename='job_apply')

urlpatterns = router.urls

# urlpatterns = router.urls + [
#     path('recruiter/notifications/', views.RecruiterNotificationsView.as_view(), name='recruiter-notifications'),
# ]