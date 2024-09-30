from operator import ipow
from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404

from .models import Post



# Create your views here.

# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by('-created_on')
#     template_name = 'index.html'

# class PostDetail(generic.DeleteView):
#     model =  Post
#     template_name =  'post_detail.html'
def post_list(request):
    post_list = Post.objects.filter(status=1).order_by('-created_on')
    context = {
        'post_list': post_list,
    }
    return render(request, 'index.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status=1)
    context = {
        'post': post,
    }
    # print(post.images.all())
    for image in post.images.all():
        print(image.image.url)
    return render(request, 'post_detail.html', context)
