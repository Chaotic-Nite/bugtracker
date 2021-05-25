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
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='New')
    assigned_user = models.ForeignKey(CustomUser, related_name='user_assigned', on_delete=models.CASCADE, blank=True, null=True)
    completed_user = models.ForeignKey(CustomUser, related_name='user_completed', on_delete=models.CASCADE, blank=True, null=True)

    # Based on Stack Overflow user JPG suggestion
    @property
    def date_diff(self):
        date_value = (self.created_at - timezone.now()).days
        date_value += 1
        return date_value