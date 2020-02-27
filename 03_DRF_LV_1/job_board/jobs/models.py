from django.db import models

# Create your models here.
class JobOffer(models.Model):
    company_name = models.CharField(max_length=60)
    company_mail = models.EmailField()
    job_title = models.CharField(max_length=70)
    job_descirption = models.TextField(default=None)
    salary = models.PositiveIntegerField()
    city = models.CharField(max_length=35)
    state = models.CharField(max_length=35)
    created_at = models.DateField(auto_now_add=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.company_name