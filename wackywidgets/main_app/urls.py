from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.WidgetCreate.as_view(), name='widgets_create'),
    path('', views.widgets_index, name='widgets_list'),
    path('/widgets', views.widgets_index, name='index'),
    path('add_widget/', views.add_widget, name='add_widget'),
]
