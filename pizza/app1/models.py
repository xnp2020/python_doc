from django.db import models

# Create your models here.
class Pizza(models.Model):
    """存储pizza的名称"""
    name = models.CharField(max_length=100)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.name

class Topping(models.Model):
    """存储pizza的原料"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField()

    def __str__(self):
        """返回模型的字符串表示"""
        return f"{self.name}"