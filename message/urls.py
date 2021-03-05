from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add-compliment/', views.add_compliment, name="add"),
]
