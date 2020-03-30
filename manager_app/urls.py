from django.urls import path
from . import views

urlpatterns = [
    # path('', views.view_list), 
    path('', views.index_view), 
    path('details/<int:manager_id>', views.details), 
    # path('add/', views.add), 
    # path('create/', views.create),
    path('update/<int:manager_id>', views.update), 
    path('manager', views.index_view),
    path('post/ajax/manager', views.post_manager, name="post_manager"),
]
