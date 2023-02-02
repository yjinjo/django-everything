from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    DetailView,
    ArchiveIndexView,
    YearArchiveView,
    MonthArchiveView,
    DayArchiveView,
)
from .models import Post
from .forms import PostForm


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else:
        form = PostForm()
        
    return render(request, "instagram/post_form.html", {"form": form})


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 10


post_list = PostListView.as_view()

post_detail = DetailView.as_view(model=Post, queryset=Post.objects.all())

post_archive = ArchiveIndexView.as_view(model=Post, date_field="created_at")

post_archive_year = YearArchiveView.as_view(model=Post, date_field="created_at")
