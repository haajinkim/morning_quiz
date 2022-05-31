from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=15)
    desc = models.TextField(max_length=256)


class Article(models.Model):
    title =  models.CharField(max_length=15)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField(max_length=256)


