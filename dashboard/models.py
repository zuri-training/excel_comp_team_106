from django.db import models

class File(models.Model):
    file1 = models.FileField(upload_to='media')
    file2 = models.FileField(upload_to='media')

    def __str__(self):
        return '{} and {}'.format(self.file1,self.file2)
