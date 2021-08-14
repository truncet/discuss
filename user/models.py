from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(max_length=20, unique=True)
    user_email = models.EmailField(unique=True)
