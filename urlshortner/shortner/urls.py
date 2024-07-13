from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),  # Note the trailing slash
    path('<str:pk>/', views.go, name='go'),  # Note the trailing slash
]