from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('new/', views.new_view, name='new'),
    path('detail/<int:pk>', views.detail_view, name='detail'),
    path('', views.category_view, name='category'),
    path('<str:name>', views.article_view, name="article")
]