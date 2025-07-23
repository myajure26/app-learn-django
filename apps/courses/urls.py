from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('details/', views.course_details, name='course_details'),
    path('lessons/', views.course_lessons, name='course_lessons'),
]
