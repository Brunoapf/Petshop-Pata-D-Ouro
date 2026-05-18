from django import forms
from .models import Pet, Servico, Agendamento


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'


class ServicoForm(forms.ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'


class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = '__all__'