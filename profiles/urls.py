from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name="profile"),
    path('orders/', views.order_page, name="order_page"),
    path('order_history/<order_number>',
         views.order_history, name="order_history"),
]
