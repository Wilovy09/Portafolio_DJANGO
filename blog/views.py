from django.shortcuts import render, get_object_or_404
from .models import post


post = post.objects.all()
def index(request):
    return render(request, 'blog.html', {'posts':post})

def post_detail(request, post_id):
    post_detail = get_object_or_404(post, pk=post_id)
    return render(request, 'post_detail.html', {'post_detail' : post_detail})