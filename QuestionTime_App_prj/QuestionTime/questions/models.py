from django.db import models
from django.conf import settings  # AUTH_USER_MODEL = "users.CustomUser"

class Question(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=240)
    slug = models.SlugField(max_length=255, unique=True)
    # vogliamo collegarlo al nostro utente CustomUser
    author = models.ForeignKey(
                    settings.AUTH_USER_MODEL,
                    on_delete=models.CASCADE,
                    related_name="questions"
                    )
    
    def __str__(self):
        return self.content


class Answer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField()
    question = models.ForeignKey(
            Question,
            on_delete=models.CASCADE,
            related_name="answers"
            )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
        )
    # mi paice alla risposta
    voters = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="votes"
    )
  
    def __str__(self):
        return self.author.username
