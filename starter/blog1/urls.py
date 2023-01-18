from django.urls import path

from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),  # localhost:8000/blog1/
]
