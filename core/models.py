from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=50)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


class VisitorsIp(models.Model):
    ip = models.TextField()

    def __str__(self):
        return str(self.ip)