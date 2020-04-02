from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_list), 
    path('details/<int:attorney_id>', views.details),
    path('add/', views.add), 
    path('create/', views.create), 
    path('update/<int:attorney_id>', views.update), 
    path('post/ajax/attorney', views.post_attorney, name="post_attorney"),
]
