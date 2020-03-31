from django.db import models

# Create your models here.
class Manager(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    # attorneys = list created by the foreign key in attorneys

    # this is used for the console and debugging purposes in the "shell"
    def __repr__(self):
        return f"Manager Name: {self.first_name} {self.last_name}"

    # This will be used to display information when editing and creating attorneys
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
