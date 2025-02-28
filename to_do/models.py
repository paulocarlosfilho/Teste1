from django.db import models



#Modelo para a lista de Tarefas
class To_do(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name='Título')
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(null=False, blank=False, verbose_name='Data Final')
    finished_at = models.DateField(null=True, blank=True)
    observacoes = models.CharField( max_length=500, null=True, blank=False)

#Modelo para a Lista de Downloads
class ArquivoDownload(models.Model):
    nome_arquivo = models.CharField(max_length=255, blank=False, verbose_name="nome_do_arquivo") # Campo para o nome do arquivo
    tipo = models.CharField(max_length=50, blank=False, verbose_name="tipo") # Campo para o tipo de arquivo (ex: PDF, CSV, PNG)
    tamanho = models.CharField(max_length=20, blank=False, verbose_name="tamanho") # Campo para o tamanho do arquivo (ex: 1.5MB, 800KB)
    arquivo = models.FileField(upload_to='downloads/', blank=False, verbose_name="arquivo") # Campo para o arquivo em si (FileField para arquivos locais)
    
    # Se você quiser usar URLs externas em vez de FileField para arquivos hospedados em outro lugar, use URLField:
    # arquivo = models.URLField(verbose_name="URL do Arquivo")

    def __str__(self):
        return self.nome_arquivo # Representação amigável do objeto no admin e em outros lugares

    class Meta:
        verbose_name = "Arquivo de Download" # Nome no singular no admin
        verbose_name_plural = "Arquivos de Download" # Nome no plural no admin