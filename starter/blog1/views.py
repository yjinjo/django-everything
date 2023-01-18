from django.shortcuts import render
from .models import Post


# Create your views here.
def post_list(request):
    # DB로 부터 모든 Post를 가져옵니다.
    qs = Post.objects.all()  # QuerySet
    return render(request, "blog1/post_list.html", {"post_list": qs})
