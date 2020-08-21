from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.utils import timezone


class Book(models.Model):
    author = models.CharField(max_length=250)
    book_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=50)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    review = models.CharField(max_length=5000, blank=True, null=True)

    def status(self):
        # self.start_date = timezone.now()
        self.end_date = timezone.now()
        self.save()

    def __str__(self):
        return self.book_title + ' - ' + self.author


# class BookCollection(models.Model):
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     review = models.TextField()

