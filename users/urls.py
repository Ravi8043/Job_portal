from django.urls import path, include
from .views import CustomRegisterView

urlpatterns = [
    path('register/', CustomRegisterView.as_view(), name='custom_register'),
    path('', include('dj_rest_auth.urls')),  # login, logout, etc.
    path('account/', include('allauth.urls')),  # required for email confirmation if using allauth
]
