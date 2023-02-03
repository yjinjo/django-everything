from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
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


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # 현재 로그인 User Instance
            post.save()
            return redirect(post)
    else:
        form = PostForm()

    return render(request, "instagram/post_form.html", {"form": form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Tip: Decorator check
    if post.author != request.user:
        messages.error(request, "작성자만 수정할 수 있습니다.")
        return redirect(post)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else:
        form = PostForm(instance=post)

    return render(request, "instagram/post_form.html", {"form": form})


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 10


post_list = PostListView.as_view()

post_detail = DetailView.as_view(model=Post, queryset=Post.objects.all())

post_archive = ArchiveIndexView.as_view(model=Post, date_field="created_at")

post_archive_year = YearArchiveView.as_view(model=Post, date_field="created_at")
