from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_activities, name='activities'),
    path('<int:activity_id>/', views.activity_details, name='activity_details')
]