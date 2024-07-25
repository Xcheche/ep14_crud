from django.db import models

# declaring tuple for branch
CHOICES = (
    ("CSE", "CSE"),
    ("IT", "IT"),
    ("ECE", "ECE"),
    ("MECH", "MECH"),
    ("CIVIL", "CIVIL"),
)


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    phone = models.PositiveIntegerField(blank=True)
    branch = models.CharField(max_length=30, choices=CHOICES)
    
    def __str__(self):
        return self.first_name
