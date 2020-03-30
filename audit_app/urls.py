from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_list), 
    path('details/<int:audit_id>', views.details),
    path('add/', views.add), 
    path('create/', views.create), 
    path('update/<int:audit_id>', views.update), 
]
