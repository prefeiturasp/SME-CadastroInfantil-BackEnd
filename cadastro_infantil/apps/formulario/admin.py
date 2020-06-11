from django.contrib import admin

from cadastro_infantil.apps.formulario.models import DadosCrianca


#
class DadosCriancaAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DadosCrianca._meta.get_fields()]
    readonly_fields = [field.attname for field in DadosCrianca._meta.fields]
    list_per_page = 25
    ordering = ('id',)

    def has_delete_permission(self, request, obj=None):
        pass

    def has_change_permission(self, request, obj=None):
        pass

    def has_add_permission(self, request):
        pass


admin.site.register(DadosCrianca, DadosCriancaAdmin)
