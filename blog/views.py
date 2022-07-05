from django.shortcuts import render
from .models import Post

from django.views.generic import ListView, DetailView

# django에서 제공하는 ListView 상속받아서 사용
class PostList(ListView):
    model = Post
    ordering = '-pk'
    # template_name = 'blog/index.html' #이부분 없애고 html을 post_list.html로 바꿔도 됨
    #템플릿에서 post_list로 사용해야함

    #list로 쭉 보여주는 것을 사용하고 싶다면 모델명막 적어줘도 된다.

# def index(request):
#     posts = Post.objects.all().order_by('-pk')
#
#     return render(
#         request,
#         'blog/post_list.html',
#         {
#             'posts' : posts,
#         }
#     )


class PostDetail(DetailView):
    model = Post


# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#
#     return render(
#         request,
#         'blog/single_page.html',
#         {
#             'post' : post
#         }
#     )