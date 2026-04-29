from django.contrib import admin
from .models import Dia, Concerto, Banda, Palco

admin.site.register(Banda)
admin.site.register(Dia)
admin.site.register(Palco)

class ConcertoAdmin(admin.ModelAdmin):
    list_display = ('banda', 'dia', 'hora', 'palco')
    list_filter = ('dia', 'palco')
    search_fields = ('banda__nome',)

    list_editable = ('dia', 'hora', 'palco')

admin.site.register(Concerto, ConcertoAdmin)
