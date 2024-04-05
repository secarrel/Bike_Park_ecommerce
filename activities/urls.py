from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_activities, name='activities'),
    path('<int:activity_id>/', views.activity_details, name='activity_details'),
    path('manage_activities/', views.manage_activities, name='manage_activities'),
    path('manage_timeslots/', views.manage_timeslots, name='manage_timeslots'),
    path('add_activity/', views.add_activity, name='add_activity'),
    path('add_timeslot/', views.add_timeslot, name='add_timeslot'),
    path('edit_activity/<int:activity_id>/', views.edit_activity, name='edit_activity'),
    path('edit_timeslot/<int:timeslot_id>/', views.edit_timeslot, name='edit_timeslot'),

]