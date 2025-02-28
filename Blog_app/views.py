from django.shortcuts import render, get_object_or_404, redirect
from Blog_app.forms import PostForm  # Ensure PostForm is imported
from .models import Post, Comment  # Ensure models are imported


def homepage(request):
    """View to display all blog posts on the homepage"""
    posts = Post.objects.all().order_by("-created_at")  # Get all posts, latest first
    total_posts = posts.count()  # Count the total number of posts
    return render(request, "Blog_app/homepage.html", {"posts": posts, "total_posts": total_posts})


def post_detail(request, post_id):
    """View to display a single blog post and handle comment submissions"""
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        name = request.POST.get("name")
        text = request.POST.get("text")  # ✅ Fixed: Using 'text' instead of 'content'
        if name and text:  # Ensure both fields are filled before creating a comment
            Comment.objects.create(post=post, name=name, text=text)
            return redirect("post_detail", post_id=post.id)  # Redirect to the same page after submitting

    return render(request, "Blog_app/detail.html", {"post": post})


def create_post(request):
    """View to create a new blog post"""
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homepage")  # Redirect to home after saving
    else:
        form = PostForm()

    return render(request, "Blog_app/create_post.html", {"form": form})
