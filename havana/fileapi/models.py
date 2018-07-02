from django.db import models

# Create your models here.
class files(models.Model):
    file_name = models.CharField(max_length = 200)
    file_attach = models.BinaryField(default=b'')
