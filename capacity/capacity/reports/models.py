from django.db import models

class Report(models.Model):

    name = models.ForeignKey(
        "locations.Location",
        related_name = 'reports',
        verbose_name = 'Спортобъект',
        on_delete=models.CASCADE
    )

    date = models.DateTimeField(
        "Дата заполнения",
        auto_now=True,
        auto_now_add=False
    )

    time_start = models.TimeField(
        "Время начала",
        auto_now=False,
        auto_now_add=False
    )

