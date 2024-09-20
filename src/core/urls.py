from django.urls import path

from src.core.views import *

urlpatterns = [
        path("student/", StudentView.as_view()),
        path("students/<int:id>/", StudentDetailView.as_view()),

]
