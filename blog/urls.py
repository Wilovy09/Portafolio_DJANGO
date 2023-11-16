from django.urls import path
from .views import index, post_detail

app_name= 'blog'

urlpatterns = [
    path('', index, name='posts'),
    path('<int:post_id>', post_detail, name='post_detail'),
]
