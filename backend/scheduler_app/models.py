from django.db import models

class Schedule(models.Model):
    home = models.CharField(max_length=100)
    away = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    game_date = models.DateField()
    game_time = models.TimeField()
    note = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.away} vs. {self.home}'
