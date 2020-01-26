from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('<int:pk>/', views.item_detail, name='item_detail'),
    path('new/', views.item_new, name='item_new'),
    path('edit/<int:pk>/', views.item_edit, name='item_edit')
]
