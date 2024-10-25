from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Checklist(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("checklists_detail", kwargs={"pk": self.id})
