from django.db import models
from django.utils import timezone
from bug_user_app.models import CustomUser

class BugTicket(models.Model):
    STATUS_CHOICES = (
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
        ('Invalid', 'Invalid')
    )

    title = models.CharField(max_length=150)
    created_at = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    filed_user = models.ForeignKey(CustomUser, related_name='user_problem', on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    assigned_user = models.ForeignKey(CustomUser, related_name='user_assigned', on_delete=models.CASCADE)
    completed_user = models.ForeignKey(CustomUser, related_name='user_completed', on_delete=models.CASCADE)

