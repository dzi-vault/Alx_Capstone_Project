from django.db import models
from users.models import User

class ManufacturerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    contact_email = models.EmailField()

    def __str__(self):
        return f"{self.company_name} ({self.user.username})"

# Create your models here.
