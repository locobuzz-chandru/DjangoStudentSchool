from django.urls import path
from . import views

urlpatterns = [
    path('school', views.SchoolAPI.as_view()),
    path('school/<int:pk>/', views.SchoolAPI.as_view()),
    path('student', views.StudentAPI.as_view()),
    path('student/<int:pk>/', views.StudentAPI.as_view()),
]
