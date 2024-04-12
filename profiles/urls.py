from django.urls import path
from . import views

urlpatterns = [
     path('',
          views.profile, name='profile'
          ),
     path('order_history/<int:user_id>/',
          views.order_history,
          name='order_history'
          ),
     path('user_details/',
          views.user_details,
          name='user_details'
          ),
     path('order_details/<order_number>',
          views.order_details,
          name='order_details'
          ),
     path('add_review/<int:activity_id>/',
          views.add_review,
          name='add_review'
          ),
     path(
        'edit_review/<int:activity_id>/',
        views.edit_review,
        name='edit_review'
        ),
]
