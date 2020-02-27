from django.urls import path
from jobs.api.views import JobListCreateAPIView, JobDetailAPIView


# Define here ENDPOINT

urlpatterns = [
    path('jobs/', 
    JobListCreateAPIView.as_view(),
    name="job-list"),

    path('jobs/<int:pk>', 
    JobDetailAPIView.as_view(),
    name="job-detail")

]