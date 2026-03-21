from django.contrib.auth.models import AbstractUser
from django.db import models


class AppUser(AbstractUser):
    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
