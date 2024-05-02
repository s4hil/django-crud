from django.db import models

# Create your models here.

class users(models.Model):
    # user_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()

    def __str__(self):
        return self.name