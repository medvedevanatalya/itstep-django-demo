from django.db import models
from django.db.models import fields as f


# Create your models here.
class Task(models.Model):
    # id = f.IntegerField()
    text = f.TextField(null=False)
    date_added = f.DateTimeField()
    date_completed = f.DateTimeField()
