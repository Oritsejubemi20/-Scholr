from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    subject = models.CharField(max_length=50)
    question_text = models.TextField()
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=1)
    explanation = models.TextField(blank=True)

    def __str__(self):
        return f"{self.subject}: {self.question_text[:50]}"
