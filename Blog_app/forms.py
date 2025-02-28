from django import forms
from .models import Comment, Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "text"]  # ✅ Use 'text' instead of 'content'


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body"]  # Add "thumbnail" if needed