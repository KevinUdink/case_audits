from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view), 
    path('details/<int:manager_id>', views.details), 
    path('update/<int:manager_id>', views.update), 
    path('manager', views.index_view),
    path('post/ajax/manager', views.post_manager, name="post_manager"),
]
