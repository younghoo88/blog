from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


# view는 모델과 템플릿을 연결해주는 역할을 한다.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print(post.pk)
    print(post.id)
    return render(request, 'blog/post_detail.html', {'post': post})
