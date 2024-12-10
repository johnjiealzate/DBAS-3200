from django.urls import path
from . import views

urlpatterns = [
    path('', views.trip_list, name='trip_list'),
    path('create/', views.create_trip, name='create_trip'),
    path('<int:pk>/update/', views.update_trip, name='update_trip'),
    path('<int:pk>/delete/', views.delete_trip, name='delete_trip'),
    path('trip/<int:id>/', views.trip_detail, name='trip_detail'),
   ]