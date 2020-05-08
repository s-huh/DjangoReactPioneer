from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=30)
    player_count = models.PositiveIntegerField(default=3)
    terrain = models.CharField(max_length=30)
    points_to_victory = models.PositiveIntegerField(default=10)
    created_at = models.DateTimeField(auto_now_add=True)