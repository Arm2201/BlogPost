from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()  # Ensure this matches your template
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Post ID: {self.id}"



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")  # Ensure Post is recognized here
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.post.title}"
