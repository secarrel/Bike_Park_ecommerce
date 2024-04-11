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
]
