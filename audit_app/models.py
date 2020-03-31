from django.db import models

# Create your models here.
class AuditType(models.Model):
    name = models.CharField(max_length=50)
    is_current = models.BooleanField(default=True)
    # attorneys is a list of Attorney - from the foreign key in the Attorney class
    # audit_criteria is a list of criteria - from the foreign key in AuditCriteria class
    # case_audits is a list of audits done using this audit type - from the CaseAudit class
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class AuditCriteria(models.Model):
    question = models.TextField()
    max_points = models.IntegerField()
    audit_type = models.ForeignKey(AuditType, on_delete=models.CASCADE, related_name="audit_criteria")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

