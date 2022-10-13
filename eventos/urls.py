# Django
from django.urls import path
# app main
from apps.main.views import Home
from apps.admin.views import Admin

urlpatterns = [
    path('', Home.as_view()),
    path('admin', Admin.as_view())
]