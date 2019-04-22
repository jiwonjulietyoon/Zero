# TODOS urls.py

from django.urls import path
from . import views

app_name = "todos"

urlpatterns = [
    path('', views.list, name="list"),
    path('create_memo/', views.create_memo, name="create_memo"),
    path('create_label/', views.create_label, name="create_label"),
    path('labels/', views.labels, name="labels"),
    path('labels/<int:label_id>/edit/', views.edit_label, name="edit_label"),
]