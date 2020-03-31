from django.db import models
from attorney_app.models import Attorney
from audit_app.models import AuditType, AuditCriteria

# Create your models here.
class CaseAudit(models.Model):
    case_number = models.CharField(max_length=30)
    case_date = models.DateField()
    judge = models.CharField(max_length=50)
    audit_type = models.ForeignKey(AuditType, on_delete=models.CASCADE, related_name="case_audits")
    attorney = models.ForeignKey(Attorney, on_delete=models.CASCADE, related_name="case_audits")
    # case_audit_criteria is a list of the criteria and scores for this audit - created from the CaseAuditCriteria class
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# each case audit will have multiple answered criteria to go along with them
#   each instance of this class will be associated with a Single case audit
class CaseAuditCriteria(models.Model):
    score = models.IntegerField()
    # allow the comments to remain empty - this will make it optional
    comment = models.TextField(blank=True)
    case_audit = models.ForeignKey(CaseAudit, on_delete=models.CASCADE, related_name="case_audit_criteria")
    # this is so we can access the questions and max points
    audit_criteria = models.ForeignKey(AuditCriteria, on_delete=models.CASCADE, related_name="case_audit_criteria")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
