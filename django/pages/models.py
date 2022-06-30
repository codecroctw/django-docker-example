from tabnanny import verbose
from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=255, default='title')

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'

    def __str__(self):
        return self.title
