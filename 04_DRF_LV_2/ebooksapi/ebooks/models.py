from django.db import models
from django.core.validators import MinValueValidator,MaxLengthValidator
from django.contrib.auth.models import User


# Create your models here.
class Ebook(models.Model):
    title = models.CharField(max_length=140)
    author = models.CharField(max_length=60)
    descriptiom = models.TextField()
    publication_date = models.DateField()

    def __str__(self):
        return self.title

class Review(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    # rating = models.PositiveIntegerField(validators=[MinValueValidator(1),
    #                                             MaxLengthValidator(5)])
    rating = models.CharField(max_length=4)
    review = models.TextField(blank=True, null=True)
    # review_author = models.CharField(max_length=8, blank=True, null=True)
    review_author = models.ForeignKey(User, on_delete=models.CASCADE)
    ebook = models.ForeignKey(Ebook,
                            on_delete=models.CASCADE,
                            related_name="reviews")

    # def __str__(self):
    #     return str(self.rating)
    def __str__(self):
        return str(self.rating)
