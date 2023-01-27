from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import render
from .models import Post


# post_list = ListView.as_view(model=Post)

# Create your views here.
def post_list(request):
    qs = Post.objects.all()
    q = request.GET.get("q", "")

    if q:
        qs = qs.filter(message__icontains=q)
    # instagram/templates/instagram/post_list.html
    return render(
        request,
        "instagram/post_list.html",
        {"post_list": qs, "q": q},
    )


def archives_year(request, year):
    return HttpResponse(f"{year}년 archives")
