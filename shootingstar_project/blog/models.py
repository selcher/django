from django.db import models
from django.utils import timezone


# Create your models here.
class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides
    self-updating ''created'' and ''modified'' fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStampedModel):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    published = models.DateTimeField(blank=True)

    def publish(self):
        self.published = timezone.now()
        self.save()

    def __str__(self):
        return self.title

