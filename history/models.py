from django.db import models

class AuditLog(models.Model):

    junction = models.ForeignKey( "junctions.Junction", on_delete=models.PROTECT, related_name="audit_logs")
    event_type = models.CharField(max_length=50)
    message = models.TextField(blank=True)
    direction = models.CharField( max_length=10, blank=True)
    previous_state = models.CharField( max_length=10, blank=True)
    new_state = models.CharField( max_length=10, blank=True)
    command = models.ForeignKey( "controllers.ControllerCommand", on_delete=models.PROTECT, related_name="audit_logs", null=True, blank=True)
    actor = models.CharField( max_length=100, default="SYSTEM")
    metadata = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.event_type} - {self.junction.name}"
