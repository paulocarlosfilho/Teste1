from django.db import models




class To_do(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Título')
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(null=False, blank=False, verbose_name='Data Final')
    fineshed_at = models.DateField(null=True, blank=False)
    observacoes = models.CharField( max_length=500, null=True, blank=False)

