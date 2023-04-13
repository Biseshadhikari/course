from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length =2000)
    content = models.TextField()
    password = models.CharField(max_length=200)
    is_verified = models.BooleanField(default=False)
    slug = models.SlugField(blank=True,null=True)
    def __str__(self) :
        return self.title

class Lessons(models.Model):
    title = models.CharField(max_length = 200)
    body = models.TextField()
    course = models.ForeignKey(Course,related_name='lessons',on_delete=models.CASCADE)

    