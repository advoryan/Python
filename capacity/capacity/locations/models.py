from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Location(models.Model):

    name = models.CharField(
        "Название спортивного объекта",
        null = False,
        blank = False,
        max_length = 200
    )
    
    user = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Спортобъект'
        verbose_name_plural = 'Спортобъекты'