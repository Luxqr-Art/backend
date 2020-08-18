from django.urls import path
from . import views
urlpatterns = [
    path('', views.json),
    path('resp/', views.resp),
    path('html/', views.html),


]