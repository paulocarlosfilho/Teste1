from django.db import models




class To_do(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateTimeField(null=False, blank=False)
    fineshed_at = models.DateTimeField(null=True, blank=False)
    observacoes = models.CharField( max_length=500, null=True, blank=False)

