from django.contrib import admin
from core.models import Evento

# Register your models here.

# Definindo os campos que devem ser exibidos referente a tabela (classe)
# Evento no console de administração.
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'data_evento', 'data_criacao')

# Registrando a classe Evento do core.models e a classe EventoAdmin no admin
admin.site.register(Evento, EventoAdmin)