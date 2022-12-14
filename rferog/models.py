from django.db import models
import uuid

class Topic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField()
    content = models.TextField()
    author = models.CharField(default='', max_length=100)
    parent_topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        default=None
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('id',)

class Upvote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.CharField(max_length=100)
    parent_post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id

    class Meta:
        ordering = ('user_id',)

class Downvote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.CharField(max_length=100)
    parent_post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id

    class Meta:
        ordering = ('user_id',)

class Comment(models.Model):
    parent_comment_id = models.CharField(max_length=100, null=True)
    content = models.TextField()
    author = models.CharField(default='', max_length=100)
    parent_post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

    class Meta:
        ordering = ('id',)
