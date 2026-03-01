
from django.urls import path, include
from . import views

urlpatterns = [
    path('jobs/', views.JobsView),
    path('jobs/<int:pk>/', views.jobDetailsView),

]
