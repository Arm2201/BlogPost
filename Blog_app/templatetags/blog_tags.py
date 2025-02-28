from django import template
from django.utils.safestring import mark_safe
from Blog_app.models import Comment, Post
import markdown

# Register template tags
register = template.Library()

@register.inclusion_tag('Blog_app/latest_posts.html')  # ✅ Ensure path matches your project structure
def show_latest_posts(count=5):
    """Fetch the latest `count` posts and display them in a template."""
    latest_posts = Post.objects.order_by('-created_at')[:count]
    return {'latest_posts': latest_posts}

@register.filter(name='markdown')
def markdown_format(text):
    """Convert Markdown text to HTML."""
    return mark_safe(markdown.markdown(text))

@register.simple_tag
def total_posts():
    """Return the total number of published posts."""
    return Post.objects.count()

@register.filter(name='comment_count')
def comment_count(post):
    """Returns the number of comments for a given post."""
    return Comment.objects.filter(post=post).count()
