from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('email-report/', views.email_page, name="email_page"),
]
