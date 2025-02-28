from django.urls import path
from .views import create_post, homepage, post_detail

urlpatterns = [
    path("", homepage, name="homepage"),
    path("post/<int:post_id>/", post_detail, name="post_detail"),
    path('create/', create_post, name='create_post'),  # URL for Create Post
]
