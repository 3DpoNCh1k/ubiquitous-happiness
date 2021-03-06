from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.urls import reverse

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
    def popular(self):
        return self.order_by('-rating')

def default_user():
    return User.objects.get_or_create(username="anon")[0].id

class Question(models.Model):
    title = models.CharField(max_length=1000)
    # text = models.CharField(max_length=1000)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, 
                               blank=True, null=True)
    likes = models.ManyToManyField(User, related_name="liked_questions")
    
    objects = QuestionManager()
    
    def get_url(self):
        return reverse("qa:question", kwargs={"question_id": self.id})
    

class Answer(models.Model):
    # text = models.CharField(max_length=1000)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, 
                               blank=True, null=True)
    
    
