from django.db import models

# learning_notes
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio_app/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title




class Project_study(models.Model):
    CATEGORY_CHOICES = [
        ('FINANCE', 'FINANCE'),
        ('BUSINESS', 'BUSINESS'),
        ('AUTOBIOGRAPHY', 'AUTOBIOGRAPHY'),
        ('COMIC', 'COMIC'),
        ('PSYCHOLOGY', 'PSYCHOLOGY'),
        ('SOCIETY', 'SOCIETY'),
        ('EFFICIENCY', 'EFFICIENCY'),
        ('NOVEL', 'NOVEL'),
        ('PHILOSOPHY', 'PHILOSOPHY'),
    ]
    CATEGORY_CHOICES_2 = [
        ('FINANCE', 'FINANCE'),
        ('BUSINESS', 'BUSINESS'),
        ('AUTOBIOGRAPHY', 'AUTOBIOGRAPHY'),
        ('COMIC', 'COMIC'),
        ('PSYCHOLOGY', 'PSYCHOLOGY'),
        ('SOCIETY', 'SOCIETY'),
        ('EFFICIENCY', 'EFFICIENCY'),
        ('NOVEL', 'NOVEL'),
        ('PHILOSOPHY', 'PHILOSOPHY'),
    ]
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    another = models.CharField(max_length=50, choices=CATEGORY_CHOICES_2)
    url = models.URLField(blank=False)