from django.db import models

# Create your models here.
class BookCredential(models.Model):
    b_name=models.CharField(max_length=255)
    chapter=models.CharField(max_length=255)
    summary=models.TextField()
    ch_content=models.TextField()
    author=models.CharField(max_length=255)
    status=models.CharField(max_length=255)

class Meta:
    db_table="Book_credentials"