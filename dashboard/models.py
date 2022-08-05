from django.db import models

class File(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='files/%Y/%m/%d/')

    def __str__(self):
        return self.title