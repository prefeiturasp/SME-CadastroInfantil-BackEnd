from django.contrib import admin

from cadastro_infantil.apps.formulario.models import DadosCrianca


#
class DadosCriancaAdmin(admin.ModelAdmin):
    # fields = '__all__'
    readonly_fields = [field.attname for field in DadosCrianca._meta.fields]
    ordering = ('id',)

    def has_delete_permission(self, request, obj=None):
        pass

    def has_change_permission(self, request, obj=None):
        pass

    def has_add_permission(self, request):
        pass


admin.site.register(DadosCrianca, DadosCriancaAdmin)
