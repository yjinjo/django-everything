from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    ArchiveIndexView,
    YearArchiveView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from .forms import PostForm


# @login_required
# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get("q", "")
#     if q:
#         qs = qs.filter(message__icontinas=q)
#
#     messages.info(request, "messages 테스트")
#
#     return render(
#         request,
#         "instagram/post_list.html",
#         {
#             "post_list": qs,
#             "q": q,
#         },
#     )


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 10


post_list = PostListView.as_view()


# @login_required
# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(
#         request,
#         "instagram/post_detail.html",
#         {
#             "post": post,
#             "object": post,
#         },
#     )


# post_detail = DetailView.as_view(model=Post, queryset=Post.objects.all())


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public=True)
        return qs


post_detail = PostDetailView.as_view()


# @login_required
# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user  # 현재 로그인 User Instance
#             post.save()
#             messages.success(request, "포스팅을 저장했습니다.")
#             return redirect(post)
#     else:
#         form = PostForm()
#
#     return render(request, "instagram/post_form.html", {"form": form, "post": None})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        messages.success(self.request, "포스팅을 저장했습니다.")
        return super().form_valid(form)


post_new = PostCreateView.as_view()


# @login_required
# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     # Tip: Decorator check
#     if post.author != request.user:
#         messages.error(request, "작성자만 수정할 수 있습니다.")
#         return redirect(post)
#
#     if request.method == "POST":
#         form = PostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             post = form.save()
#             messages.success(request, "포스팅을 수정했습니다.")
#             return redirect(post)
#     else:
#         form = PostForm(instance=post)
#
#     return render(request, "instagram/post_form.html", {"form": form, "post": post})


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        messages.success(self.request, "포스팅을 수정했습니다.")
        return super().form_valid(form)


post_edit = PostUpdateView.as_view()


# @login_required
# def post_delete(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     if request.method == "POST":
#         post.delete()
#         messages.success(request, "포스팅을 삭제했습니다.")
#         return redirect("instagram:post_list")
#
#     return render(
#         request,
#         "instagram/post_confirm_delete.html",
#         {"post": post},
#     )


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post

    success_url = reverse_lazy("instagram:post_list")

    # def get_success_url(self):
    #     return reverse("instagram:post_list")


post_delete = PostDeleteView.as_view()

post_archive = ArchiveIndexView.as_view(model=Post, date_field="created_at")

post_archive_year = YearArchiveView.as_view(model=Post, date_field="created_at")
