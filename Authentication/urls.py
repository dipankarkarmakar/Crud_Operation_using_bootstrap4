from django.urls import path

from Authentication import views

urlpatterns = [
    path('', views.person_list, name='person_list'),
    path('person_view/<int:pk>/', views.person_view, name='person_view'),
    path('new/', views.person_create, name='person_new'),
    path('edit/<int:pk>/', views.person_update, name='person_edit'),
    path('delete/<int:pk>/', views.person_delete, name='person_delete'),

]
