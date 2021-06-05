from django.urls import path
from .views import (
    dailyApiCall
)

urlpatterns = [
    path('home/', dailyApiCall, name="Daily Count")
]
