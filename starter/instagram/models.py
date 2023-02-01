from django.db import models

from django.conf import settings
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to="instagram/post/%Y/%m/%d")
    tag_set = models.ManyToManyField("Tag", blank=True)
    is_public = models.BooleanField(default=False, verbose_name="공개여부")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-id"]

    def get_absolute_url(self):
        return reverse("instagram:post_detail", args=[self.pk])

    # 객체에 대한 문자열 표현
    def __str__(self):
        return self.message


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, limit_choices_to={"is_public": True}
    )
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    # 하나의 태그는 unique함을 가지는 게 맞습니다.
    name = models.CharField(max_length=50, unique=True)

    # post_set = models.ManyToManyField(Post)

    def __str__(self):
        return self.name
