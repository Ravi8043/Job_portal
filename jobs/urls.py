from rest_framework import routers
from . import views
router = routers.SimpleRouter()

router.register('jobs',views.JobPostingView, basename='jobs')
router.register('jobapply',views.JobApplicationView, basename='job_apply')

urlpatterns = router.urls