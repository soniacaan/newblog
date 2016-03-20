from django.db import models

from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    related_title = models.CharField(max_length=200, blank=True)
    recipe_type = models.CharField(max_length=400, blank=True)
    city_recipe = models.CharField(max_length=400, blank=True)
    country_recipe = models.CharField(max_length=400, blank=True)
    family = models.CharField(max_length=200, blank=True)
    city_history = models.CharField(max_length=400, blank=True)
    country_history = models.CharField(max_length=400, blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
