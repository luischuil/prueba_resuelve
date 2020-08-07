from django.urls import include, path
from rest_framework import routers
from . import views

urlpatterns = [
    path('payroll_resuelve', views.payroll_resuelve, name='payroll_resuelve'),
    path('payroll_teams', views.payroll_teams, name='payroll_teams'),
]