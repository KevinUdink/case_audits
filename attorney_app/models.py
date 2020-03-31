from django.db import models
from manager_app.models import Manager

# Create your models here.
class Attorney(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name="attorneys")
    # need to still add the foreign key for default audit type
    # audit_type = models.ForeignKey(AuditType, on_delete=models.CASCADE, related_name="attorneys")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    # this is used for the console and debugging purposes in the "shell"
    def __repr__(self):
        return f"Attorney Name: {self.first_name} {self.last_name}"

    # This will be used to display information when editing and creating attorneys
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

