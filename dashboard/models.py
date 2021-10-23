from enum import Enum
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Link(models.Model):
    BASIC = 'BASIC'
    SPOTIFY = 'SPOTIFY'
    YOUTUBE = 'YOUTUBE'

    LINK_TYPE_CHOICES = [
        (BASIC, 'basic'),
        (SPOTIFY, 'spotify'),
        (YOUTUBE, 'youtube'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=200, db_column="url")
    # type = models.CharField(max_length=200, choices=LINK_TYPE_CHOICES, default=BASIC)
    is_active = models.BooleanField()


    def embed_url(self):
        return self.url[:25] + 'embed/' + self.url[25:]

    # @url.setter
    # def url(self, value):
    #     self._url = value