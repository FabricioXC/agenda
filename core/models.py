from django.db import models

# Create your models here.

class Evento(models.Model):
    # verbose_name define o nome que será utilizado para exibição na coluna
    titulo = models.CharField(max_length=100, verbose_name='Título')
    descricao = models.TextField(blank=True, null=True, verbose_name='Descrição')
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    # auto_now=True insere a hora atual no campo sempre que for criado um novo registro
    data_criacao = models.DateTimeField(auto_now=True, verbose_name='Data de Criação')

    # Metadados. Definir o nome da tabela. Caso contrário, o Django escolhe o nome.
    class Meta: 
        db_table = 'evento'

    # Sempre que for chamado o objeto título, será trazido o nome do título.
    # Desta forma, ao invés de aparecer o nome do evento como Evento Object()
    # no console de administração, o nome trará o título do evento.
    def __str__(self):
        return self.titulo
