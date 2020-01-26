from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('<int:pk>/', views.item_detail, name='item_detail'),
    path('new/', views.item_new, name='item_new'),
    path('edit/<int:pk>/', views.item_edit, name='item_edit'),
    path('delete/<int:pk>/', views.item_delete, name='item_delete'),
    path('count/<int:pk>', views.item_count, name='item_count'),

    path('accounts/', views.account_list, name='account_list'),
    path('accounts/<int:pk>/', views.account_detail, name='account_detail'),
    path('accounts/new/', views.account_new, name='account_new'),
    path('accounts/edit/<int:pk>/', views.account_edit, name='account_edit'),
    path('accounts/delete/<int:pk>/', views.account_delete, name='account_delete'),
]
