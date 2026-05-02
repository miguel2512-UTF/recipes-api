from django.db import models
from authentication.models import User

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    ingredients = models.JSONField(default=dict)
    time = models.CharField(max_length=30)
    difficulty = models.CharField(max_length=20, choices=[("easy", "Facil"), ("middle", "Medio"), ("hard", "dificil")])
    category = models.CharField(max_length=200, choices=[("breakfast","desayuno"), ("vegan", "vegano"), ("fast", "rapido"), ("desserts", "postres"), ("drinks", "bebidas")])
    image = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ("user", "recipe")