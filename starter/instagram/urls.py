from django.urls import path, re_path, register_converter

from . import views
from .converters import YearConverter

register_converter(YearConverter, "year")

app_name = "instagram"  # URL Reverse 에서 namespace 역할을 하게 됩니다.
urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("new/", views.post_new, name="post_new"),
    path("<int:pk>", views.post_detail, name="post_detail"),
    path("archive/", views.post_archive, name="post_archive"),
    path("archive/<int:year>/", views.post_archive_year, name="post_archive_year"),
]
