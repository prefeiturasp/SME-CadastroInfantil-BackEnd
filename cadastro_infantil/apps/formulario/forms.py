from django import forms

class InativacaoForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        data_inicio = cleaned_data.get("data_inicio")
        data_fim = cleaned_data.get("data_fim")
        if data_fim < data_inicio:
            raise forms.ValidationError("Data fim precisa ser maior ou igual a data de início.")
