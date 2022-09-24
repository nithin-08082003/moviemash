from django.db import models

# Create your models here.

class Feedback(models.Model):
    name =  models.CharField(max_length=50,blank=False)
    feedback_text = models.TextField(blank=False, max_length=300)
    posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.feedback_text[0:50]

    class Meta:
        ordering = ['-posted']
