from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):

    EXAM_TYPE_CHOICES = [
        ('JAMB', 'JAMB'),
        ('WAEC', 'WAEC'),
        ('NECO', 'NECO'),
        ('POST_UTME', 'Post-UTME'),
    ]

    SUBJECT_CHOICES = [
        ('biology', 'Biology'),
        ('chemistry', 'Chemistry'),
        ('physics', 'Physics'),
        ('mathematics', 'Mathematics'),
        ('english', 'English'),
    ]

    exam_type = models.CharField(max_length=20, choices=EXAM_TYPE_CHOICES, default='JAMB')
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES, default='physics')
    year = models.IntegerField(default=2020)
    question_text = models.TextField()
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=1)
    explanation = models.TextField(blank=True)

    def __str__(self):
        return f"{self.exam_type} {self.subject} {self.year}: {self.question_text[:50]}"
